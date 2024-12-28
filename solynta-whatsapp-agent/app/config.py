from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    OPENAI_API_KEY: Optional[str] = "dummy_openai_key"
    WHATSAPP_API_KEY: Optional[str] = "dummy_whatsapp_key"
    WHATSAPP_API_URL: Optional[str] = "https://api.whatsapp.com/v1"
    REDIS_URL: Optional[str] = "redis://localhost:6379"
    DATABASE_URL: Optional[str] = "sqlite:///./test.db"

    class Config:
        env_file = ".env"