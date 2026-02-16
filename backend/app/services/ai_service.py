import json
import time
from google import genai
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, select
from app.core.config import settings
from app.schemas.task import MicroWin, TaskStreamChunk
from app.models.task import MicroWinModel, Task
from app.models.user import User
from app.core.security import encrypt_data, decrypt_data

# Initialize Gemini Client
client = genai.Client(api_key=settings.GEMINI_API_KEY)

async def stream_micro_wins(safe_instruction: str, task_id: int, user_id: int, db: AsyncSession):
    """
    Fetches user neuro-profile, customizes the prompt, and streams tasks.
    Includes latency metrics as SSE events to satisfy the <5s requirement.
    """
    # ─── Latency Timer Start ──────────────────────────────────
    t_start = time.perf_counter()
    first_token_emitted = False

    # 1. Fetch User Profile for Individualization
    user_result = await db.execute(select(User).where(User.id == user_id))
    user = user_result.scalar_one_or_none()
    
    # Decrypt preferences if they exist
    preferences = decrypt_data(user.encrypted_preferences) if user and user.encrypted_preferences else "None"
    struggles = decrypt_data(user.encrypted_struggle_areas) if user and user.encrypted_struggle_areas else "None"
    granularity = user.granularity_level if user else 3

    # 2. The Personalized Prompt
    # This fulfills the 'Individualized Neuro-Profile' requirement
    prompt = (
        f"You are a neuro-inclusive executive function coach.\n"
        f"User Struggles: {struggles}\n"
        f"User Preferences: {preferences}\n"
        f"Granularity Level: {granularity}/5 (1=Broad steps, 5=Tiny, single-action steps)\n\n"
        f"Goal: {safe_instruction}\n\n"
        "Instructions:\n"
        "1. First, output a 3-4 word title for this task.\n"
        f"2. Based on granularity {granularity}, break the goal into 3-5 actions. "
        "3. If granularity is high, ensure actions are sensory-grounded (e.g., 'Touch the cold handle' instead of 'Open fridge').\n"
        "4. STRICT OUTPUT FORMAT (One JSON per line):\n"
        "{\"title\": \"...\"}\n"
        "{\"action\": \"...\"}\n"
        "{\"status\": \"end\"}"
    )

    try:
        stream = client.models.generate_content_stream(
            model='gemini-2.5-flash', # Using Flash for < 5s latency requirement
            contents=prompt
        )

        buffer = ""
        step_counter = 1
        
        for chunk in stream:
            if chunk.text:
                # ─── Time-to-First-Token ──────────────────────
                if not first_token_emitted:
                    ttft_ms = round((time.perf_counter() - t_start) * 1000)
                    yield f"data: {{\"latency_ms\": {ttft_ms}}}\n\n"
                    first_token_emitted = True

                buffer += chunk.text
                
                if "\n" in buffer:
                    lines = buffer.split("\n")
                    for line in lines[:-1]:
                        line = line.strip()
                        if not line: continue
                        
                        try:
                            raw_data = json.loads(line)

                            # Handle AI-Generated Title
                            if "title" in raw_data:
                                stmt = update(Task).where(Task.id == task_id).values(title=raw_data["title"])
                                await db.execute(stmt)
                                await db.commit()
                                yield f"data: {{\"sidebar_title\": \"{raw_data['title']}\"}}\n\n"
                                continue
                            
                            if raw_data.get("status") == "end":
                                # ─── Total Latency ────────────────────
                                total_ms = round((time.perf_counter() - t_start) * 1000)
                                yield f"data: {{\"total_latency_ms\": {total_ms}}}\n\n"
                                return 

                            action_text = raw_data.get("action")
                            if action_text:
                                # Encrypting for Privacy-First Cloud storage
                                encrypted_action = encrypt_data(action_text)
                                
                                new_step = MicroWinModel(
                                    task_id=task_id,
                                    encrypted_action=encrypted_action,
                                    is_completed=False,
                                    step_order=step_counter
                                )
                                db.add(new_step)
                                await db.commit()

                                # Yield for UI
                                chunk_data = TaskStreamChunk(
                                    id=task_id,
                                    original_goal=safe_instruction,
                                    current_step=MicroWin(
                                        step_id=step_counter,
                                        action=action_text
                                    )
                                )
                                yield f"data: {chunk_data.model_dump_json()}\n\n"
                                step_counter += 1

                        except json.JSONDecodeError:
                            continue
                    
                    buffer = lines[-1]

        # If stream ends without explicit "end" status, still emit total latency
        total_ms = round((time.perf_counter() - t_start) * 1000)
        yield f"data: {{\"total_latency_ms\": {total_ms}}}\n\n"

    except Exception as e:
        yield f"data: {{\"error\": \"AI Stream Error: {str(e)}\"}}\n\n"