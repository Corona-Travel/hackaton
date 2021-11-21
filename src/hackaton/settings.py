from functools import lru_cache

from pydantic import BaseSettings, AnyUrl


class Settings(BaseSettings):
    app_name: str = "Corona Travel Microservices"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
