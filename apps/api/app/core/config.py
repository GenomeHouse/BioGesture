from functools import lru_cache
import os


class Settings:
    app_name: str = os.getenv("BIOGESTURE_APP_NAME", "BioGesture API")
    version: str = os.getenv("BIOGESTURE_VERSION", "0.1.0")
    api_prefix: str = os.getenv("BIOGESTURE_API_PREFIX", "/api/v1")
    cors_origins: tuple[str, ...] = tuple(
        origin.strip()
        for origin in os.getenv("BIOGESTURE_CORS_ORIGINS", "http://localhost:3000").split(",")
        if origin.strip()
    )
    api_key: str | None = os.getenv("BIOGESTURE_API_KEY") or None


@lru_cache
def get_settings() -> Settings:
    return Settings()
