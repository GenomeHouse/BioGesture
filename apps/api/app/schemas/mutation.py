from typing import Literal
from pydantic import BaseModel, Field


class MutationRequest(BaseModel):
    position: int = Field(ge=0)
    alternate: Literal["A", "C", "G", "T", "N"]


class MutationResult(BaseModel):
    sequence_id: str
    position: int
    reference: str
    alternate: str
    sequence: str
    consequence: Literal["synonymous", "missense", "unknown"]
