import logging
from typing import Any, List, Dict, Optional
from app.config import settings

logger = logging.getLogger(__name__)

_pool = None

# In-memory storage fallback when running in Demo Mode
_demo_documents_db: List[Dict[str, Any]] = []
_demo_chunks_db: List[Dict[str, Any]] = []
_demo_id_counter = 1

def init_oracle_db():
    """Initialize python-oracledb pool or prepare demo in-memory storage."""
    global _pool, _demo_documents_db, _demo_chunks_db, _demo_id_counter
    if settings.is_demo_mode:
        logger.info("[Oracle DB] APP_ENV=development: Running in-memory database simulation mode.")
        if not _demo_documents_db:
            # Seed initial demo document
            _demo_documents_db.append({
                "id": 1,
                "document_name": "OCI_Architecture_Overview.pdf",
                "storage_object_name": "demo_oci_architecture.pdf",
                "file_type": "application/pdf",
                "file_size_bytes": 1048576,
                "ocr_status": "COMPLETED",
                "confidence_score": 98.5,
                "created_at": "2026-09-05 10:00:00"
            })
            _demo_id_counter = 2
        return None

    try:
        import oracledb
        # Set up Oracle Wallet if provided
        wallet_kwargs = {}
        if settings.ORACLE_DB_WALLET_LOCATION:
            wallet_kwargs["config_dir"] = settings.ORACLE_DB_WALLET_LOCATION
            wallet_kwargs["wallet_location"] = settings.ORACLE_DB_WALLET_LOCATION
            if settings.ORACLE_DB_WALLET_PASSWORD:
                wallet_kwargs["wallet_password"] = settings.ORACLE_DB_WALLET_PASSWORD

        _pool = oracledb.create_pool(
            user=settings.ORACLE_DB_USER,
            password=settings.ORACLE_DB_PASSWORD,
            dsn=settings.ORACLE_DB_DSN,
            min=1,
            max=5,
            increment=1,
            **wallet_kwargs
        )
        logger.info(f"[Oracle DB 23ai] Successfully created connection pool to DSN: {settings.ORACLE_DB_DSN}")
        return _pool
    except Exception as e:
        logger.error(f"[Oracle DB 23ai] Connection failed: {e}. Falling back to demo mode.")
        return None

def get_db_connection():
    """Yield a connection from pool or None for demo mode."""
    if settings.is_demo_mode or _pool is None:
        return None
    return _pool.acquire()
