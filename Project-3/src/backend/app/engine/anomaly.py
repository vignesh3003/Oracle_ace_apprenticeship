import numpy as np
import logging
from typing import Dict, Any, Optional, Tuple
from app.engine.oci_ons import publish_ons_alert

logger = logging.getLogger(__name__)

# Sliding window buffer for calculating mean & standard deviation
_cpu_window = [25.0, 30.0, 28.0, 32.0, 29.0, 31.0, 27.0]

def evaluate_anomaly(metric: Dict[str, Any]) -> Tuple[bool, Optional[Dict[str, Any]]]:
    """
    Calculate Z-score for CPU utilization:
    Z = (observed - mean) / std_dev
    If Z > 2.5 or CPU > 85.0%, trigger anomaly & publish OCI ONS notification.
    """
    global _cpu_window
    cpu = float(metric.get("cpu_utilization_pct", 0.0))
    _cpu_window.append(cpu)
    if len(_cpu_window) > 30:
        _cpu_window.pop(0)

    mean = np.mean(_cpu_window)
    std = np.std(_cpu_window)
    if std == 0:
        std = 1.0

    z_score = float((cpu - mean) / std)

    is_anomaly = z_score > 2.5 or cpu > 85.0
    if is_anomaly:
        host = metric.get("host_name", "unknown_host")
        logger.warning(f"[ANOMALY DETECTED] Host {host} CPU Spike: {cpu}% (Z-Score: {z_score:.2f})")

        subject = f"⚠️ OCI TELEMETRY ALERT: CPU Spike on {host}"
        body = f"""
        ORACLE TELEMETRYX CRITICAL ANOMALY ALERT
        ------------------------------------------
        Host Name: {host}
        Metric Type: CPU Utilization
        Observed Value: {cpu}%
        Threshold Value: 85.0%
        Calculated Z-Score: {z_score:.2f}
        Timestamp: 2026-09-05T12:50:00Z
        
        Action Required: Inspect OCI Compute instance resource allocation.
        """
        # Publish real-time OCI ONS notification
        ons_sent = publish_ons_alert(subject, body)

        alert_record = {
            "host_name": host,
            "metric_type": "CPU",
            "observed_value": cpu,
            "threshold_value": 85.0,
            "z_score": round(z_score, 2),
            "ons_notification_status": "SENT" if ons_sent else "FAILED"
        }
        return True, alert_record

    return False, None
