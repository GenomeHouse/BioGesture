from datetime import datetime, timezone
from uuid import uuid4

_experiments: dict[str, dict[str, object]] = {}


def list_experiments() -> list[dict[str, object]]:
    return list(_experiments.values())


def create_experiment(name: str, sequence_id: str, model: str) -> dict[str, object]:
    experiment = {
        "id": str(uuid4()),
        "name": name,
        "sequence_id": sequence_id,
        "model": model,
        "status": "queued",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _experiments[str(experiment["id"])] = experiment
    return experiment
