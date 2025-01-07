"""
Configuration settings for the Safi Farm API.
"""
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings."""
    
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Safi Farm API"
    
    # Security
    SECRET_KEY: str = "development_key"  # TODO: Change in production
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # Database
    DATABASE_URL: str = "sqlite:///./safifarm.db"  # TODO: Configure for production
    
    # CORS
    BACKEND_CORS_ORIGINS: list[str] = ["*"]  # TODO: Configure for production
    
    class Config:
        case_sensitive = True
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings() 