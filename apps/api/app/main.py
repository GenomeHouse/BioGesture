from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.v1.router import router as v1_router
from .core.config import get_settings
from .core.logging import configure_logging
from .websocket.gesture_stream import router as gesture_router

settings = get_settings()
configure_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="Sequence analysis and gesture-control services for BioGesture.",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=list(settings.cors_origins),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(v1_router, prefix=settings.api_prefix)
app.include_router(gesture_router)


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok", "service": "biogesture-api"}
