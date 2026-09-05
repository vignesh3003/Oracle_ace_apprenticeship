# OracleTelemetryX: Real-Time Monitoring & Anomaly Alerting System

[![OCI Compute ARM](https://img.shields.io/badge/OCI-Ampere%20ARM-orange.svg)](https://www.oracle.com/cloud/compute/arm/)
[![OCI ONS](https://img.shields.io/badge/OCI-Notification%20Service-red.svg)](https://www.oracle.com/cloud/cloud-native/notifications/)
[![Oracle Database](https://img.shields.io/badge/Oracle-Autonomous%20DB-blue.svg)](https://www.oracle.com/database/autonomous-database/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A real-time infrastructure telemetry monitoring and statistical anomaly detection platform hosted on **OCI Always Free Ampere A1 Compute (ARM64)**, utilizing **`python-oracledb` SessionPool connection pooling** for high-throughput metric ingestion into **Oracle Autonomous Database** and triggering automated alerts via **OCI Notification Service (ONS)** topics.

---

## Architecture

```text
Telemetry Agent Daemon (OCI Ampere Compute VM)
       │
       ▼
FastAPI Ingestion Engine (python-oracledb SessionPool)
       ├───► Oracle Autonomous Database (Time-Series Metric Tables)
       └───► OCI Notification Service - ONS (Topic Email Alert)
```

---

## Features
- ⚡ **OCI Ampere ARM VM Deployment:** Production-grade deployment on OCI Always Free Ampere ARM64.
- 🏊 **High-Throughput Connection Pooling:** Uses `python-oracledb` SessionPool for low-latency writes.
- 📈 **Z-Score Anomaly Engine:** Identifies CPU/RAM resource spikes automatically.
- 🔔 **Real-Time ONS Email Alerts:** Publishes alerts to OCI Notification Service topics.
- 📊 **Next.js SRE Console:** Live telemetry streams and anomaly history views.

---

## License
[MIT License](LICENSE)
