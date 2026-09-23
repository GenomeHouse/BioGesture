from fastapi import APIRouter, Depends, status
from pydantic import BaseModel, Field

from ...core.security import require_api_key
from ...services.experiment_service import create_experiment, list_experiments

router = APIRouter(prefix="/experiments", tags=["experiments"], dependencies=[Depends(require_api_key)])


class ExperimentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    sequence_id: str
    model: str = Field(default="gesture-mlp", max_length=80)


@router.get("")
def read_experiments() -> list[dict[str, object]]:
    return list_experiments()


@router.post("", status_code=status.HTTP_201_CREATED)
def add_experiment(payload: ExperimentCreate) -> dict[str, object]:
    return create_experiment(payload.name, payload.sequence_id, payload.model)
