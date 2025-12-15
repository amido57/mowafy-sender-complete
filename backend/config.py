import os
from datetime import timedelta

class Config:
    """Application configuration."""
    
    ENV = os.getenv("ENV", "production")
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_EXPIRES = timedelta(hours=12)
    
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 10,
        "max_overflow": 20,
        "pool_pre_ping": True
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    FB_APP_ID = os.getenv("FB_APP_ID")
    FB_APP_SECRET = os.getenv("FB_APP_SECRET")
    FB_REDIRECT_URI = os.getenv("FB_REDIRECT_URI")
