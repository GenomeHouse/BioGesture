from datetime import datetime, timezone
from uuid import uuid4

from ..db.database import InMemoryDatabase
from ..db.models import SequenceRecord
from ..schemas.sequence import SequenceCreate, SequenceDetail, SequenceSummary, SequenceUpdate


def _gc_content(sequence: str) -> float:
    return round((sequence.count("G") + sequence.count("C")) / len(sequence) * 100, 2)


def _summary(record: SequenceRecord) -> SequenceSummary:
    return SequenceSummary(
        id=record.id,
        name=record.name,
        length=len(record.sequence),
        organism=record.organism,
        created_at=record.created_at,
        updated_at=record.updated_at,
    )


def _detail(record: SequenceRecord) -> SequenceDetail:
    return SequenceDetail(
        **_summary(record).model_dump(),
        sequence=record.sequence,
        description=record.description,
        gc_content=_gc_content(record.sequence),
    )


def list_sequences(database: InMemoryDatabase) -> list[SequenceSummary]:
    with database.lock:
        return [_summary(item) for item in database.sequences.values()]


def get_sequence(database: InMemoryDatabase, sequence_id: str) -> SequenceDetail | None:
    with database.lock:
        record = database.sequences.get(sequence_id)
        return _detail(record) if record else None


def create_sequence(database: InMemoryDatabase, payload: SequenceCreate) -> SequenceDetail:
    now = datetime.now(timezone.utc)
    record = SequenceRecord(
        id=str(uuid4()),
        name=payload.name,
        sequence=payload.sequence,
        description=payload.description,
        organism=payload.organism,
        created_at=now,
        updated_at=now,
    )
    with database.lock:
        database.sequences[record.id] = record
    return _detail(record)


def update_sequence(database: InMemoryDatabase, sequence_id: str, payload: SequenceUpdate) -> SequenceDetail | None:
    with database.lock:
        record = database.sequences.get(sequence_id)
        if not record:
            return None
        changes = payload.model_dump(exclude_unset=True)
        for field, value in changes.items():
            setattr(record, field, value)
        record.updated_at = datetime.now(timezone.utc)
        return _detail(record)


def delete_sequence(database: InMemoryDatabase, sequence_id: str) -> bool:
    with database.lock:
        return database.sequences.pop(sequence_id, None) is not None
