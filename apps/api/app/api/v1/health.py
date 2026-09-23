from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
def api_health() -> dict[str, str]:
    return {"status": "ok", "service": "biogesture-api", "scope": "v1"}
