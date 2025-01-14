from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Job Application Bot"
    environment: str = "development"
    api_key: str
    database_url: str

    class Config:
        env_file = ".env"

# Create a settings instance
settings = Settings()
