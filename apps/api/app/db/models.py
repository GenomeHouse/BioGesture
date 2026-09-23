from dataclasses import dataclass
from datetime import datetime, timezone


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class SequenceRecord:
    id: str
    name: str
    sequence: str
    description: str | None
    organism: str | None
    created_at: datetime
    updated_at: datetime
