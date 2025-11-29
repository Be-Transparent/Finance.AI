from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Application
    ENV: str = "development"
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"
    
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://finance:finance@localhost:5432/finance_ai"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # JWT
    JWT_SECRET_KEY: str = "your-super-secret-jwt-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    # External APIs
    MONOBANK_API_KEY: str = ""
    PRIVATBANK_API_KEY: str = ""
    DPS_API_TOKEN: str = ""
    
    # Diia
    DIIA_CLIENT_ID: str = ""
    DIIA_CLIENT_SECRET: str = ""
    DIIA_REDIRECT_URI: str = "https://finance.ai.diia.gov.ua/callback"
    
    # iQ
    IQ_CLIENT_ID: str = ""
    IQ_CLIENT_SECRET: str = ""
    IQ_BFF_URL: str = "https://iq.example.com"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
