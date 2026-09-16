import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.transcribe import router as transcribe_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ocimediastream-ai")

app = FastAPI(title=settings.APP_NAME, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["System"])
def health():
    return {"status": "healthy", "app_name": settings.APP_NAME, "environment": settings.APP_ENV}

app.include_router(transcribe_router, prefix="/api/v1")
