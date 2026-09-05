import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.router import api_router
from app.db.connection import init_oracle_db

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("oracledocu-ai")

app = FastAPI(
    title=settings.APP_NAME,
    description="Enterprise Document Intelligence & Semantic Vector Search platform powered by Oracle Autonomous Database 23ai & OCI Vision AI.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting {settings.APP_NAME} in environment: {settings.APP_ENV}")
    init_oracle_db()

@app.get("/health", tags=["System"])
async def health_check():
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "oracle_db_dsn": settings.ORACLE_DB_DSN,
        "demo_mode": settings.is_demo_mode
    }

app.include_router(api_router, prefix=settings.API_V1_PREFIX)
