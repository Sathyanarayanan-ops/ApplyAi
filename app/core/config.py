from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Job Application Bot"  # Add this attribute
    environment: str = "development"
    groq_api_key: str
    groq_endpoint: str = "https://api.groqcloud.com"

    class Config:
        env_file = ".env"

settings = Settings()
