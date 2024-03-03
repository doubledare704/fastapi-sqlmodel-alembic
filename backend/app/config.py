from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env.dev', env_file_encoding='utf-8', env_ignore_empty=True)

    # database configurations
    DATABASE_URL: str = Field(...)


def get_config() -> Config:
    return Config()