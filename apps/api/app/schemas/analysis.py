from pydantic import BaseModel, Field


class GCContentResult(BaseModel):
    sequence_id: str
    length: int
    gc_content: float
    at_content: float
    counts: dict[str, int]


class ComplementResult(BaseModel):
    sequence_id: str
    complement: str
    reverse_complement: str


class ORFResult(BaseModel):
    start: int = Field(ge=0)
    end: int = Field(gt=0)
    frame: int
    sequence: str


class ORFAnalysisResult(BaseModel):
    sequence_id: str
    orfs: list[ORFResult]


class ProteinTranslationResult(BaseModel):
    sequence_id: str
    frame: int
    protein: str
