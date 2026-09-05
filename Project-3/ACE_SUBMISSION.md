# Oracle ACE Apprentice Contribution Document

# Contribution Title
**OracleTelemetryX: Real-Time Edge-to-Cloud Monitoring & Anomaly Alerting System on OCI Ampere Compute & ONS**

# Project Overview
OracleTelemetryX is a real-time infrastructure monitoring platform deployed on OCI Always Free Ampere A1 Compute (ARM64 VM), utilizing `python-oracledb` connection pooling to write high-frequency system metrics to Oracle Autonomous Database and publishing anomaly notifications via OCI Notification Service (ONS).

# Problem Statement
High-frequency infrastructure metrics stream continuously. Storing metrics with low latency requires connection pooling to prevent DB connection overhead, while detecting spikes and dispatching alerts must occur in real-time.

# Solution
The platform uses a background agent daemon to sample system metrics, ingests data into Oracle Autonomous Database using a `python-oracledb` SessionPool, evaluates sliding-window $Z$-score anomalies, and dispatches instant email alerts via OCI Notification Service (ONS) topics.

# Oracle Technologies Used

### 1. OCI Compute (Always Free Ampere A1 ARM64)
- **What it does:** Hosts the FastAPI ingestion service and systemd telemetry daemon.
- **Why it was selected:** OCI offers up to 4 OCPUs and 24 GB RAM free on Ampere ARM architecture.
- **How it was integrated:** Deployed via Docker Compose and systemd services on Ubuntu 22.04 ARM64.

### 2. Oracle Autonomous Database (SessionPool Connection Pooling)
- **What it does:** Stores time-series metrics and anomaly audit logs.
- **Why it was selected:** Low-latency transactional DB capabilities.
- **How it was integrated:** Leveraged `python-oracledb.create_pool()` with `min=2, max=10` session instances.

### 3. OCI Notification Service (ONS)
- **What it does:** Delivers real-time email notifications when CPU spikes cross thresholds.
- **Why it was selected:** Built-in cloud notification engine.
- **How it was integrated:** Invoked `oci.ons.NotificationDataPlaneClient.publish_message`.

# My Implementation
1. Authored Python system telemetry collection daemon (`agent/telemetry_daemon.py`).
2. Formulated Oracle SQL time-series schemas with compound indexes (`host_name`, `recorded_at`).
3. Implemented sliding-window $Z$-score anomaly detection engine (`backend/app/engine/anomaly.py`).
4. Built Next.js 14 telemetry monitoring dashboard with real-time pollers.

# Architecture

```text
Telemetry Agent Daemon (OCI Ampere Compute VM)
       │
       ▼
FastAPI Ingestion Engine (python-oracledb SessionPool)
       ├───► Oracle Autonomous Database (Time-Series Metric Tables)
       └───► OCI Notification Service - ONS (Topic Email Alert)
```

# Product Usage Evidence To Capture
1. **OCI Console - Compute Instance Page:** Active Always Free Ampere A1 VM status.
2. **OCI Console - Notification Service (ONS) Topic:** Displaying topic subscriptions.
3. **Inbox Email Notification:** Real-time alert email received from OCI ONS.
4. **Oracle SQL Developer Web:** SQL query output showing time-series metric records.

# GitHub Repository
`https://github.com/your-username/oracletelemetry-x`
