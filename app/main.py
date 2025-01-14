from fastapi import FastAPI
from app.core.config import settings

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "app_name": settings.app_name,
        "environment": settings.environment
    }
