import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.metrics import router as metrics_router
from app.db.connection_pool import init_oracle_pool

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("oracletelemetry-x")

app = FastAPI(
    title=settings.APP_NAME,
    description="Real-Time Edge-to-Cloud Infrastructure Telemetry & Anomaly Detection on OCI Compute ARM & Oracle Autonomous DB.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    logger.info("Initializing Oracle Database Connection Pool...")
    init_oracle_pool()

@app.get("/health", tags=["System"])
async def health():
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "ons_topic_ocid": settings.OCI_ONS_TOPIC_OCID
    }

app.include_router(metrics_router, prefix="/api/v1")
