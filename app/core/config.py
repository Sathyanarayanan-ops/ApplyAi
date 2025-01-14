from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Job Application Bot"
    environment: str = "development"  # Can be 'development', 'staging', or 'production'
    api_key: str  # Example: An API key for accessing external services
    database_url: str  # Example: PostgreSQL or SQLite database URL

    class Config:
        env_file = ".env"

# Create a settings instance to use in the app
settings = Settings()
