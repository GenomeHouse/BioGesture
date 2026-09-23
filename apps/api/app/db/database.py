from threading import RLock

from .models import SequenceRecord


class InMemoryDatabase:
    def __init__(self) -> None:
        self.sequences: dict[str, SequenceRecord] = {}
        self.lock = RLock()


_database = InMemoryDatabase()


def get_database() -> InMemoryDatabase:
    return _database
