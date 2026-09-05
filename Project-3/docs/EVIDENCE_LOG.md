# Evidence Log — Project 3: OracleTelemetryX

This log tracks every genuine product-usage evidence item created after acceptance into the Oracle ACE Apprentice Program.

---

### Evidence ID: E01
- **Date:** 2026-09-05
- **Time:** 17:00 UTC
- **Oracle Service:** OCI Compute (Ampere A1 Flex ARM)
- **Action Performed:** Provisioned Always Free Ampere A1 Compute VM instance running Ubuntu 22.04 ARM64.
- **Result:** Instance running with 4 OCPUs and 24 GB RAM. Assigned public IP.
- **Screenshot Filename:** `evidence/COMPUTE/01-ampere-vm-instance.png`

---

### Evidence ID: E02
- **Date:** 2026-09-05
- **Time:** 17:30 UTC
- **Oracle Service:** OCI Notification Service (ONS)
- **Action Performed:** Created ONS Topic `telemetry-alerts` and subscribed target email address.
- **Result:** Email subscription confirmed and active.
- **Screenshot Filename:** `evidence/ALERTING/02-ons-topic-subscription.png`

---

### Evidence ID: E03
- **Date:** 2026-09-05
- **Time:** 18:00 UTC
- **Oracle Service:** OCI Notification Service (ONS Email Delivery)
- **Action Performed:** Triggered CPU spike anomaly ($Z$-Score $> 2.5$) in telemetry engine, causing Python SDK to call `oci.ons`.
- **Result:** Received real-time alert email from OCI ONS notification topic.
- **Screenshot Filename:** `evidence/ALERTING/03-ons-email-received.png`

---

### Evidence ID: E04
- **Date:** 2026-09-05
- **Time:** 18:30 UTC
- **Oracle Service:** Oracle Autonomous Database (Connection Pooling)
- **Action Performed:** Ingested time-series metric streams via `python-oracledb` SessionPool.
- **Result:** Executed high-throughput concurrent writes to `telemetry_metrics` table.
- **Screenshot Filename:** `evidence/DATABASE/04-db-time-series-metrics.png`

---

### Evidence ID: E05
- **Date:** 2026-09-05
- **Time:** 19:00 UTC
- **Oracle Service:** OCI Compute ARM Host Deployment
- **Action Performed:** Deployed application containers via Docker Compose on Ampere ARM VM and enabled systemd daemon.
- **Result:** Verified continuous metric ingestion and SRE dashboard availability.
- **Screenshot Filename:** `evidence/OCI/05-ssh-docker-status.png`
