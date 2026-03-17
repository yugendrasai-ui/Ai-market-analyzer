from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    OPENROUTER_API_KEY: Optional[str] = None
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    RATE_LIMIT_PER_MINUTE: int = 5
    
    # Simple Guest Auth Credentials (for exercise purposes)
    GUEST_USERNAME: str = "guest"
    GUEST_PASSWORD: str = "guest_pass_123"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
