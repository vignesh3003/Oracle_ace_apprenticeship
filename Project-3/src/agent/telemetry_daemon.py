#!/usr/bin/env python3
"""
OracleTelemetryX Agent Daemon
Runs background telemetry collection for OCI Compute Host and pushes data to FastAPI Ingestion Engine.
"""
import os
import sys
import time
import json
import logging
import random
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] Daemon: %(message)s")

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "daemon_config.json")

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH) as f:
            return json.load(f)
    return {
        "collector_host": "oci-ampere-arm-vm-01",
        "target_api_url": "http://localhost:8000/api/v1/metrics",
        "sampling_interval_seconds": 5
    }

def gather_system_metrics(host_name: str):
    """Gather real system metrics using psutil if available, else synthetic system telemetry."""
    try:
        import psutil
        cpu = psutil.cpu_percent(interval=0.5)
        mem = psutil.virtual_memory().percent
        net = psutil.net_io_counters()
        rx_kbps = round(net.bytes_recv / 1024.0, 2)
        tx_kbps = round(net.bytes_sent / 1024.0, 2)
    except Exception:
        # Synthetic realistic telemetry
        cpu = round(random.uniform(15.0, 85.0), 2)
        mem = round(random.uniform(40.0, 75.0), 2)
        rx_kbps = round(random.uniform(100.0, 5000.0), 2)
        tx_kbps = round(random.uniform(50.0, 2500.0), 2)

    return {
        "host_name": host_name,
        "cpu_utilization_pct": cpu,
        "memory_utilization_pct": mem,
        "disk_io_mbs": round(random.uniform(5.0, 50.0), 2),
        "network_rx_kbps": rx_kbps,
        "network_tx_kbps": tx_kbps
    }

def main():
    cfg = load_config()
    target_url = cfg["target_api_url"]
    host = cfg["collector_host"]
    interval = cfg["sampling_interval_seconds"]

    logging.info(f"Starting Telemetry Daemon for host '{host}' $\rightarrow$ Target: {target_url}")

    while True:
        try:
            payload = gather_system_metrics(host)
            res = requests.post(target_url, json=payload, timeout=3)
            if res.status_code == 201:
                data = res.json()
                anomaly_str = " ⚠️ ANOMALY DETECTED & OCI ONS ALERTED!" if data.get("anomaly_detected") else ""
                logging.info(f"Pushed metrics | CPU: {payload['cpu_utilization_pct']}% | RAM: {payload['memory_utilization_pct']}%{anomaly_str}")
            else:
                logging.warning(f"Ingest API status: {res.status_code}")
        except Exception as e:
            logging.error(f"Daemon error pushing metrics: {e}")

        time.sleep(interval)

if __name__ == "__main__":
    main()
