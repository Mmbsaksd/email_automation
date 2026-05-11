from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import Literal, Optional


class Settings(BaseSettings):
        
        model_config = SettingsConfigDict(env_file='.env', env_file_encoding="utf-8")

        # Azure OpenAI
        azure_openai_api_key: str
        azure_openai_endpoint: str
        azure_openai_api_version: str




        model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )