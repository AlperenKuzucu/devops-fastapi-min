from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    # APP_ENV ve APP_COMMIT olarak okunacak (env_prefix sayesinde)
    env: str = "dev"
    commit: str = "local"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        extra="ignore",
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()
