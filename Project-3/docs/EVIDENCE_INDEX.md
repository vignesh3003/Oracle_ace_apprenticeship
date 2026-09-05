# Evidence Index — Project 3: OracleTelemetryX

| ID | Evidence Title | Oracle Product | What It Demonstrates | Target Screenshot File | Status |
|---|---|---|---|---|---|
| **E01** | OCI Compute Instance Details | OCI Compute (Ampere ARM) | Active Always Free Ampere A1 Flex VM (`oci-ampere-arm-vm-01`) running Ubuntu ARM64 | `evidence/COMPUTE/01-ampere-vm-instance.png` | Pending User Capture |
| **E02** | OCI Notification Service (ONS) | OCI Notification Service | ONS Topic creation (`telemetry-alerts`) and confirmed email subscription status | `evidence/ALERTING/02-ons-topic-subscription.png` | Pending User Capture |
| **E03** | Real Email Notification Received | OCI Notification Service | Actual inbox screenshot of anomaly alert email delivered by OCI ONS | `evidence/ALERTING/03-ons-email-received.png` | Pending User Capture |
| **E04** | Oracle Database Connection Pool | Oracle Autonomous Database | Time-series metric table data stored via `python-oracledb` SessionPool | `evidence/DATABASE/04-db-time-series-metrics.png` | Pending User Capture |
| **E05** | Terminal SSH Docker Status | OCI Compute Deployment | Active SSH session on OCI Ampere VM showing `docker compose ps` running containers | `evidence/OCI/05-ssh-docker-status.png` | Pending User Capture |

---

## Detailed Capture Guidance for Submission Evidence

### Screenshot E01: OCI Compute Instance Console Details
- **Oracle Service:** OCI Compute (Ampere A1 Flex ARM)
- **Location in OCI Console:** Compute $\rightarrow$ Instances $\rightarrow$ `oci-ampere-arm-vm-01`
- **What Must Be Visible:**
  - Instance Name: `oci-ampere-arm-vm-01`
  - Shape: `VM.Standard.A1.Flex` (Ampere Arm)
  - State: `RUNNING`
  - Public IP Address
- **Save As:** `PROJECT-3/evidence/COMPUTE/01-ampere-vm-instance.png`

### Screenshot E02: OCI Notification Service (ONS) Topic
- **Oracle Service:** OCI Notification Service (ONS)
- **Location in OCI Console:** Developer Services $\rightarrow$ Application Integration $\rightarrow$ Notifications $\rightarrow$ Topics
- **What Must Be Visible:**
  - Topic Name: `telemetry-alerts`
  - Subscriptions list showing your email address with status `Confirmed`.
- **Save As:** `PROJECT-3/evidence/ALERTING/02-ons-topic-subscription.png`

### Screenshot E03: Inbox Email Alert Screenshot
- **Oracle Service:** OCI Notification Service (ONS Email Delivery)
- **Location:** Your email inbox (Gmail/Outlook)
- **What Must Be Visible:**
  - Email Sender: `noreply@notification.us-ashburn-1.oraclecloud.com`
  - Subject: `⚠️ OCI TELEMETRY ALERT: CPU Spike on oci-ampere-arm-vm-01`
  - Email Body: JSON anomaly payload containing Z-Score calculation.
- **Save As:** `PROJECT-3/evidence/ALERTING/03-ons-email-received.png`

### Screenshot E04: Time-Series Metric Table in SQL Developer Web
- **Oracle Service:** Oracle Autonomous Database (Connection Pooling)
- **Location in OCI Console:** Autonomous DB Details $\rightarrow$ Database Actions $\rightarrow$ SQL
- **What Must Be Visible:**
  - SQL Query: `SELECT * FROM telemetry_metrics ORDER BY metric_id DESC;`
  - Returned rows displaying ingested CPU/RAM metrics and host details.
- **Save As:** `PROJECT-3/evidence/DATABASE/04-db-time-series-metrics.png`

### Screenshot E05: Terminal SSH Docker Execution on OCI Compute
- **Oracle Service:** OCI Compute Host Terminal
- **Location:** Local Terminal connected via SSH to OCI VM
- **What Must Be Visible:**
  - SSH command line showing `ubuntu@oci-ampere-arm-vm-01:~$ docker compose ps`
  - Active running containers (`telemetry-backend`, `telemetry-frontend`).
- **Save As:** `PROJECT-3/evidence/OCI/05-ssh-docker-status.png`
