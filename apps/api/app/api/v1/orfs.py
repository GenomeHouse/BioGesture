from fastapi import APIRouter, Depends, HTTPException, Query

from ...core.security import require_api_key
from ...db.database import InMemoryDatabase, get_database
from ...schemas.analysis import ORFAnalysisResult
from ...services.analysis_service import find_orfs
from ...services.sequence_service import get_sequence

router = APIRouter(prefix="/orfs", tags=["orfs"], dependencies=[Depends(require_api_key)])


@router.get("/{sequence_id}", response_model=ORFAnalysisResult)
def read_orfs(
    sequence_id: str,
    minimum_length: int = Query(default=9, ge=3, le=10_000),
    database: InMemoryDatabase = Depends(get_database),
) -> ORFAnalysisResult:
    sequence = get_sequence(database, sequence_id)
    if not sequence:
        raise HTTPException(status_code=404, detail="Sequence not found")
    return find_orfs(sequence, minimum_length)
