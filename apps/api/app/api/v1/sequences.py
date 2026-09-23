from fastapi import APIRouter, Depends, HTTPException, Query, status

from ...core.security import require_api_key
from ...db.database import InMemoryDatabase, get_database
from ...schemas.sequence import SequenceCreate, SequenceDetail, SequenceSummary, SequenceUpdate
from ...services.sequence_service import create_sequence, delete_sequence, get_sequence, list_sequences, update_sequence

router = APIRouter(prefix="/sequences", tags=["sequences"], dependencies=[Depends(require_api_key)])


@router.get("", response_model=list[SequenceSummary])
def read_sequences(
    search: str | None = Query(default=None, max_length=120),
    database: InMemoryDatabase = Depends(get_database),
) -> list[SequenceSummary]:
    sequences = list_sequences(database)
    if search:
        term = search.casefold()
        sequences = [item for item in sequences if term in item.name.casefold() or term in (item.organism or "").casefold()]
    return sequences


@router.post("", response_model=SequenceDetail, status_code=status.HTTP_201_CREATED)
def add_sequence(payload: SequenceCreate, database: InMemoryDatabase = Depends(get_database)) -> SequenceDetail:
    return create_sequence(database, payload)


@router.get("/{sequence_id}", response_model=SequenceDetail)
def read_sequence(sequence_id: str, database: InMemoryDatabase = Depends(get_database)) -> SequenceDetail:
    sequence = get_sequence(database, sequence_id)
    if not sequence:
        raise HTTPException(status_code=404, detail="Sequence not found")
    return sequence


@router.patch("/{sequence_id}", response_model=SequenceDetail)
def edit_sequence(sequence_id: str, payload: SequenceUpdate, database: InMemoryDatabase = Depends(get_database)) -> SequenceDetail:
    sequence = update_sequence(database, sequence_id, payload)
    if not sequence:
        raise HTTPException(status_code=404, detail="Sequence not found")
    return sequence


@router.delete("/{sequence_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_sequence(sequence_id: str, database: InMemoryDatabase = Depends(get_database)) -> None:
    if not delete_sequence(database, sequence_id):
        raise HTTPException(status_code=404, detail="Sequence not found")
