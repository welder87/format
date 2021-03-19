from pydantic import BaseSettings
from functools import lru_cache


class Config(BaseSettings):
    SECRET_KEY: str
    DEBUG: bool
    ALLOWED_HOSTS: list[str]

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    return Config()


project_settings = get_settings()
