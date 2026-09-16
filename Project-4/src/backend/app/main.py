import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.chat import router as chat_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("oraclegenai-rag")

app = FastAPI(
    title=settings.APP_NAME,
    description="Enterprise Knowledge Assistant powered by OCI Generative AI Service & Oracle Autonomous Database.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["System"])
def health():
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "genai_model": settings.OCI_GENAI_MODEL_ID
    }

app.include_router(chat_router, prefix="/api/v1")
