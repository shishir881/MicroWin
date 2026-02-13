import json
from google import genai
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update
from app.core.config import settings
from app.schemas.task import MicroWin, TaskStreamChunk
from app.models.task import MicroWinModel
from app.core.security import encrypt_data
from app.models.task import Task

# Initialize Gemini Client
client = genai.Client(api_key=settings.GEMINI_API_KEY)

async def stream_micro_wins(safe_instruction: str, task_id: int, db: AsyncSession):
    """
    Streams 3-5 steps from AI. 
    Uses a terminator JSON {"status": "end"} to force the last meaningful step 
    out of the buffer for database persistence.
    """
    prompt = (
        f"Goal: {safe_instruction}\n"
        "First, generate a concise 3-4 word title for this task (e.g., 'Mastering Python Basics'). "
        "Then, break the goal into 3 to 5 tiny actions. "
        "Output format: "
        "Line 1: {\"title\": \"...\"}\n"
        "Following lines: {\"action\": \"...\"}\n"
        "Final line: {\"status\": \"end\"}"
    )

    try:
        # Start content stream
        stream = client.models.generate_content_stream(
            model='gemini-2.5-flash', 
            contents=prompt
        )

        buffer = ""
        step_counter = 1
        
        for chunk in stream:
            if chunk.text:
                buffer += chunk.text
                
                # Check for newlines to identify completed JSON lines
                if "\n" in buffer:
                    lines = buffer.split("\n")
                    
                    # Process all complete lines found so far
                    for line in lines[:-1]:
                        line = line.strip()
                        if not line:
                            continue
                        
                        try:
                            raw_data = json.loads(line)

                            # for title file
                            if "title" in raw_data:
                                # Update the Task record in Neon with the AI-generated title
                                stmt = update(Task).where(Task.id == task_id).values(title=raw_data["title"])
                                await db.execute(stmt)
                                await db.commit()
                                # Optional: Yield the title to the frontend so the sidebar updates live
                                yield f"data: {{\"sidebar_title\": \"{raw_data['title']}\"}}\n\n"
                                continue
                            
                            # TERMINATOR HACK: If status is 'end', the stream is done.
                            # We don't save or yield this line.
                            if raw_data.get("status") == "end":
                                return 

                            action_text = raw_data.get("action")
                            if action_text:
                                # 1. Encrypt and Save to Neon Cloud
                                encrypted_action = encrypt_data(action_text)
                                new_step = MicroWinModel(
                                    task_id=task_id,
                                    encrypted_action=encrypted_action,
                                    is_completed=False,
                                    step_order=step_counter
                                )
                                db.add(new_step)
                                await db.commit()

                                # 2. Format and Yield for the UI
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
                            # Skip lines that aren't valid JSON yet
                            continue
                    
                    # Keep the remaining partial data in the buffer
                    buffer = lines[-1]

    except Exception as e:
        yield f"data: {{\"error\": \"AI Stream Error: {str(e)}\"}}\n\n"