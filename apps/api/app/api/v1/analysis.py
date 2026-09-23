from fastapi import APIRouter, Depends, HTTPException

from ...core.security import require_api_key
from ...db.database import InMemoryDatabase, get_database
from ...schemas.analysis import ComplementResult, GCContentResult, ProteinTranslationResult
from ...services.analysis_service import complement, gc_content, translate
from ...services.sequence_service import get_sequence

router = APIRouter(prefix="/analysis", tags=["analysis"], dependencies=[Depends(require_api_key)])


def _sequence_or_404(sequence_id: str, database: InMemoryDatabase):
    sequence = get_sequence(database, sequence_id)
    if not sequence:
        raise HTTPException(status_code=404, detail="Sequence not found")
    return sequence


@router.get("/{sequence_id}/gc-content", response_model=GCContentResult)
def read_gc_content(sequence_id: str, database: InMemoryDatabase = Depends(get_database)) -> GCContentResult:
    return gc_content(_sequence_or_404(sequence_id, database))


@router.get("/{sequence_id}/complement", response_model=ComplementResult)
def read_complement(sequence_id: str, database: InMemoryDatabase = Depends(get_database)) -> ComplementResult:
    return complement(_sequence_or_404(sequence_id, database))


@router.get("/{sequence_id}/translation", response_model=ProteinTranslationResult)
def read_translation(sequence_id: str, frame: int = 0, database: InMemoryDatabase = Depends(get_database)) -> ProteinTranslationResult:
    try:
        return translate(_sequence_or_404(sequence_id, database), frame)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error
