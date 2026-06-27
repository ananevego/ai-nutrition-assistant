import os

class Settings:
    def __init__(self):
        self.app_name = os.getenv("APP_NAME", "AI Nutrition Assistant")
        self.app_version = os.getenv("APP_VERSION", "1.0.0")

settings = Settings()
