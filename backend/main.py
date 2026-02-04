#fastapi ko endpoints haru banaucha
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from app.services.pii_services import mask_pii
from app.services.ai_service import stream_micro_wins
from app.schemas.task import TaskRequest

app = FastAPI()

@app.post("/api/v1/decompose/stream")
async def process_streaming_task(request: TaskRequest):
    # Step 1: Scrub PII (Must happen BEFORE the stream starts)
    safe_instruction = mask_pii(request.instruction)
    
    # Step 2: Return a Stream
    # The frontend will start receiving data IMMEDIATELY
    return StreamingResponse(
        stream_micro_wins(safe_instruction), 
        media_type="text/event-stream"
    )