#!/usr/bin/env bash
# =============================================================================
# Install Telemetry Daemon as Systemd Service on OCI Ampere Compute Instance
# =============================================================================

echo "Installing OracleTelemetryX daemon service on OCI Ampere VM..."

sudo cat <<EOF > /etc/systemd/system/oracletelemetry.service
[Unit]
Description=OracleTelemetryX Ingestion Agent Daemon
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/oracletelemetry-x
ExecStart=/usr/bin/python3 agent/telemetry_daemon.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable oracletelemetry.service
sudo systemctl start oracletelemetry.service

echo "Service status:"
sudo systemctl status oracletelemetry.service --no-pager
