import os

class Settings:
    app_name = os.getenv("APP_NAME", "AI Nutrition Assistant")
    app_version = os.getenv("APP_VERSION", "1.0.0.")

settings = Settings()