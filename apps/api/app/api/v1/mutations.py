from fastapi import APIRouter, Depends, HTTPException

from ...core.security import require_api_key
from ...db.database import InMemoryDatabase, get_database
from ...schemas.mutation import MutationRequest, MutationResult
from ...services.sequence_service import get_sequence

router = APIRouter(prefix="/mutations", tags=["mutations"], dependencies=[Depends(require_api_key)])


@router.post("/{sequence_id}", response_model=MutationResult)
def apply_mutation(
    sequence_id: str,
    payload: MutationRequest,
    database: InMemoryDatabase = Depends(get_database),
) -> MutationResult:
    sequence = get_sequence(database, sequence_id)
    if not sequence:
        raise HTTPException(status_code=404, detail="Sequence not found")
    if payload.position >= sequence.length:
        raise HTTPException(status_code=400, detail="Mutation position is outside the sequence")
    reference = sequence.sequence[payload.position]
    if reference == payload.alternate:
        raise HTTPException(status_code=400, detail="Alternate base must differ from reference")
    mutated = sequence.sequence[:payload.position] + payload.alternate + sequence.sequence[payload.position + 1:]
    return MutationResult(
        sequence_id=sequence_id,
        position=payload.position,
        reference=reference,
        alternate=payload.alternate,
        sequence=mutated,
        consequence="unknown",
    )
