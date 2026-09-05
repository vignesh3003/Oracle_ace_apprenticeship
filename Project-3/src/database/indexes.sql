-- Create Indexes for fast time-series queries and anomaly lookup
CREATE INDEX IF NOT EXISTS idx_metrics_host_time ON telemetry_metrics (host_name, recorded_at DESC);
CREATE INDEX IF NOT EXISTS idx_anomalies_time ON telemetry_anomalies (created_at DESC);
