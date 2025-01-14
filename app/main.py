from fastapi import FastAPI
from app.core.config import settings
from app.api.endpoints import router as api_router

app = FastAPI()


# Include the API router
app.include_router(api_router, prefix="/api")


@app.get("/")
def read_root():
    return {
        "app_name": settings.app_name,
        "environment": settings.environment
    }
