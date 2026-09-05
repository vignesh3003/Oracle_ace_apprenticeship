import logging
from typing import List, Optional
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from app.db.time_series import insert_telemetry_metric, insert_anomaly_alert, get_recent_metrics, get_recent_anomalies
from app.engine.anomaly import evaluate_anomaly

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/metrics", tags=["Telemetry Ingestion"])

class MetricPayload(BaseModel):
    host_name: str = Field(..., example="oci-ampere-arm-vm-01")
    cpu_utilization_pct: float = Field(..., ge=0.0, le=100.0)
    memory_utilization_pct: float = Field(..., ge=0.0, le=100.0)
    disk_io_mbs: Optional[float] = 0.0
    network_rx_kbps: Optional[float] = 0.0
    network_tx_kbps: Optional[float] = 0.0

@router.post("", status_code=status.HTTP_201_CREATED)
async def ingest_telemetry(payload: MetricPayload):
    """
    Ingest system telemetry $\rightarrow$ write to Oracle Autonomous DB via SessionPool $\rightarrow$ run Z-score anomaly engine.
    """
    try:
        metric_dict = payload.dict()
        m_id = insert_telemetry_metric(metric_dict)

        # Anomaly evaluation
        is_anomaly, alert_dict = evaluate_anomaly(metric_dict)
        if is_anomaly and alert_dict:
            alert_dict["metric_id"] = m_id
            insert_anomaly_alert(alert_dict)

        return {
            "status": "ingested",
            "metric_id": m_id,
            "anomaly_detected": is_anomaly,
            "oracle_services": ["OCI Compute (Ampere ARM)", "Oracle Autonomous DB Connection Pool", "OCI Notification Service (ONS)"]
        }
    except Exception as e:
        logger.error(f"Metric ingestion error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history")
async def fetch_metric_history(limit: int = 20):
    """Fetch time-series telemetry records from Oracle DB."""
    return get_recent_metrics(limit=limit)

@router.get("/anomalies")
async def fetch_anomalies(limit: int = 10):
    """Fetch anomaly alerts and OCI ONS notification logs from Oracle DB."""
    return get_recent_anomalies(limit=limit)
