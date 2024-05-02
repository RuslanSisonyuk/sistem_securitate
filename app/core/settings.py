import logging
import os
from functools import lru_cache

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    LOG_LEVEL: str | int = os.getenv("LOG_LEVEL", logging.INFO)
    DB_HOST: str = os.getenv("DB_HOST", "")
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_NAME: str = os.getenv("DB_NAME", "")
    DB_USER: str = os.getenv("DB_USER", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")

    DB_URL: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


@lru_cache
def get_settings() -> Settings:
    return Settings()
