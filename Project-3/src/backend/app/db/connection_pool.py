import logging
from typing import Any, List, Dict
from app.config import settings

logger = logging.getLogger(__name__)

_pool = None
_demo_metrics_db: List[Dict[str, Any]] = []
_demo_anomalies_db: List[Dict[str, Any]] = []
_metric_id_seq = 1
_alert_id_seq = 1

def init_oracle_pool():
    """Create high-throughput python-oracledb SessionPool for Oracle Autonomous DB."""
    global _pool
    if settings.is_demo_mode:
        logger.info("[Oracle DB Pool] Running in Demo Simulation Mode.")
        return None

    try:
        import oracledb
        wallet_kwargs = {}
        if settings.ORACLE_DB_WALLET_LOCATION:
            wallet_kwargs["config_dir"] = settings.ORACLE_DB_WALLET_LOCATION
            wallet_kwargs["wallet_location"] = settings.ORACLE_DB_WALLET_LOCATION

        _pool = oracledb.create_pool(
            user=settings.ORACLE_DB_USER,
            password=settings.ORACLE_DB_PASSWORD,
            dsn=settings.ORACLE_DB_DSN,
            min=settings.ORACLE_DB_POOL_MIN,
            max=settings.ORACLE_DB_POOL_MAX,
            increment=1,
            **wallet_kwargs
        )
        logger.info(f"[Oracle DB Pool] SessionPool created. Min={settings.ORACLE_DB_POOL_MIN}, Max={settings.ORACLE_DB_POOL_MAX}")
        return _pool
    except Exception as e:
        logger.error(f"[Oracle DB Pool] Connection pool creation failed: {e}")
        return None

def acquire_connection():
    if settings.is_demo_mode or _pool is None:
        return None
    return _pool.acquire()
