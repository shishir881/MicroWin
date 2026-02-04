from pydantic import BaseModel, Field, ConfigDict
from typing import List

class MicroWin(BaseModel):
    step_id: int
    action: str
    is_completed: bool = False

class TaskCreate(BaseModel):
    # User le input pathaune model
    instruction: str = Field(..., min_length=5, example="Clean my room")

class TaskRead(BaseModel):
    # API le response dine model
    id: int
    original_goal: str
    micro_wins: List[MicroWin]
    
    # SQLAlchemy model sanga integrate garna
    model_config = ConfigDict(from_attributes=True)