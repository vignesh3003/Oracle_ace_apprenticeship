-- =============================================================================
-- OracleTelemetryX: Database Schema for High-Throughput Time-Series Metrics
-- Target: Oracle Autonomous Database (OLTP / Transaction Processing)
-- =============================================================================

-- 1. Create Telemetry Time-Series Metrics Table
CREATE TABLE IF NOT EXISTS telemetry_metrics (
    metric_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    host_name VARCHAR2(150) NOT NULL,
    cpu_utilization_pct NUMBER(5, 2) NOT NULL,
    memory_utilization_pct NUMBER(5, 2) NOT NULL,
    disk_io_mbs NUMBER(8, 2),
    network_rx_kbps NUMBER(10, 2),
    network_tx_kbps NUMBER(10, 2),
    recorded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Create Anomaly Alerts Table
CREATE TABLE IF NOT EXISTS telemetry_anomalies (
    alert_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    metric_id NUMBER REFERENCES telemetry_metrics(metric_id) ON DELETE CASCADE,
    host_name VARCHAR2(150) NOT NULL,
    metric_type VARCHAR2(50) NOT NULL,     -- 'CPU', 'MEMORY', 'NETWORK'
    observed_value NUMBER(8, 2) NOT NULL,
    threshold_value NUMBER(8, 2) NOT NULL,
    z_score NUMBER(6, 2) NOT NULL,
    ons_notification_status VARCHAR2(50) DEFAULT 'SENT',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

COMMIT;
