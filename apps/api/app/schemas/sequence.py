from datetime import datetime
from pydantic import BaseModel, Field, field_validator


class SequenceCreate(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    sequence: str = Field(min_length=1, max_length=2_000_000)
    description: str | None = Field(default=None, max_length=500)
    organism: str | None = Field(default=None, max_length=120)

    @field_validator("sequence")
    @classmethod
    def normalize_sequence(cls, value: str) -> str:
        normalized = "".join(value.upper().split())
        invalid = set(normalized) - set("ACGTN")
        if not normalized:
            raise ValueError("Sequence cannot be empty")
        if invalid:
            raise ValueError(f"Invalid DNA bases: {''.join(sorted(invalid))}")
        return normalized


class SequenceUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=500)


class SequenceSummary(BaseModel):
    id: str
    name: str
    length: int
    organism: str | None
    created_at: datetime
    updated_at: datetime


class SequenceDetail(SequenceSummary):
    sequence: str
    description: str | None
    gc_content: float
