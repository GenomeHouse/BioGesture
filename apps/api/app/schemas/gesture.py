from datetime import datetime
from pydantic import BaseModel, Field


class GestureEvent(BaseModel):
    gesture: str = Field(min_length=1, max_length=64)
    confidence: float = Field(ge=0, le=1)
    timestamp: datetime | None = None
    hand: str | None = Field(default=None, max_length=16)


class GestureRecognition(BaseModel):
    gesture: str
    confidence: float
    accepted: bool
    received_at: datetime


class GestureSession(BaseModel):
    session_id: str
    connected: bool
    last_gesture: GestureRecognition | None = None
