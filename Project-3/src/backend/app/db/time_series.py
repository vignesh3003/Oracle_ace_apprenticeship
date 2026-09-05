import logging
from typing import Dict, Any, List
from app.db.connection_pool import acquire_connection, _demo_metrics_db, _demo_anomalies_db, _metric_id_seq, _alert_id_seq
from app.config import settings

logger = logging.getLogger(__name__)

def insert_telemetry_metric(metric: Dict[str, Any]) -> int:
    global _metric_id_seq
    conn = acquire_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            sql = """
                INSERT INTO telemetry_metrics (host_name, cpu_utilization_pct, memory_utilization_pct, disk_io_mbs, network_rx_kbps, network_tx_kbps)
                VALUES (:1, :2, :3, :4, :5, :6)
                RETURNING metric_id INTO :7
            """
            out_var = cursor.var(int)
            cursor.execute(sql, (
                metric["host_name"],
                metric["cpu_utilization_pct"],
                metric["memory_utilization_pct"],
                metric.get("disk_io_mbs", 0.0),
                metric.get("network_rx_kbps", 0.0),
                metric.get("network_tx_kbps", 0.0),
                out_var
            ))
            conn.commit()
            m_id = out_var.getvalue()[0]
            cursor.close()
            conn.close()
            return m_id
        except Exception as e:
            logger.error(f"Failed to insert metric into Oracle DB: {e}")
            if conn: conn.close()

    # Demo Simulation Fallback
    m_id = _metric_id_seq
    _metric_id_seq += 1
    metric["metric_id"] = m_id
    metric["recorded_at"] = "2026-09-05 12:50:00"
    _demo_metrics_db.insert(0, metric)
    return m_id

def insert_anomaly_alert(alert: Dict[str, Any]) -> int:
    global _alert_id_seq
    conn = acquire_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            sql = """
                INSERT INTO telemetry_anomalies (metric_id, host_name, metric_type, observed_value, threshold_value, z_score, ons_notification_status)
                VALUES (:1, :2, :3, :4, :5, :6, :7)
                RETURNING alert_id INTO :8
            """
            out_var = cursor.var(int)
            cursor.execute(sql, (
                alert["metric_id"],
                alert["host_name"],
                alert["metric_type"],
                alert["observed_value"],
                alert["threshold_value"],
                alert["z_score"],
                alert.get("ons_notification_status", "SENT"),
                out_var
            ))
            conn.commit()
            a_id = out_var.getvalue()[0]
            cursor.close()
            conn.close()
            return a_id
        except Exception as e:
            logger.error(f"Failed to insert anomaly alert into Oracle DB: {e}")
            if conn: conn.close()

    a_id = _alert_id_seq
    _alert_id_seq += 1
    alert["alert_id"] = a_id
    alert["created_at"] = "2026-09-05 12:50:00"
    _demo_anomalies_db.insert(0, alert)
    return a_id

def get_recent_metrics(limit: int = 20) -> List[Dict[str, Any]]:
    conn = acquire_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT metric_id, host_name, cpu_utilization_pct, memory_utilization_pct, disk_io_mbs, network_rx_kbps, network_tx_kbps, recorded_at
                FROM telemetry_metrics
                ORDER BY metric_id DESC
                FETCH FIRST :1 ROWS ONLY
            """, (limit,))
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            return [{
                "metric_id": r[0], "host_name": r[1], "cpu_utilization_pct": float(r[2]),
                "memory_utilization_pct": float(r[3]), "disk_io_mbs": float(r[4] or 0),
                "network_rx_kbps": float(r[5] or 0), "network_tx_kbps": float(r[6] or 0),
                "recorded_at": str(r[7])
            } for r in rows]
        except Exception as e:
            logger.error(f"Failed to fetch metrics: {e}")
            if conn: conn.close()

    return _demo_metrics_db[:limit]

def get_recent_anomalies(limit: int = 10) -> List[Dict[str, Any]]:
    conn = acquire_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT alert_id, metric_id, host_name, metric_type, observed_value, threshold_value, z_score, ons_notification_status, created_at
                FROM telemetry_anomalies
                ORDER BY alert_id DESC
                FETCH FIRST :1 ROWS ONLY
            """, (limit,))
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            return [{
                "alert_id": r[0], "metric_id": r[1], "host_name": r[2], "metric_type": r[3],
                "observed_value": float(r[4]), "threshold_value": float(r[5]), "z_score": float(r[6]),
                "ons_notification_status": r[7], "created_at": str(r[8])
            } for r in rows]
        except Exception as e:
            logger.error(f"Failed to fetch anomalies: {e}")
            if conn: conn.close()

    return _demo_anomalies_db[:limit]
