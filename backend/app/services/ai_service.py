# uses the LLM model for MicroWin AI services
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def stream_micro_wins(safe_text: str):
    # We tell the AI to stream the response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Break this into 3 tiny steps: {safe_text}"}],
        stream=True  # THIS IS THE KEY
    )

    for chunk in response:
        if chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            # We "yield" each word as it arrives
            yield f"data: {content}\n\n"