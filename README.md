# Oracle ACE Apprentice – Product Usage Milestone Contributions

This repository contains my hands-on Oracle technology projects created for my **Oracle ACE Apprentice** journey. The projects demonstrate genuine Oracle product usage across cloud infrastructure, autonomous databases, AI services, and serverless architectures.

- Each project is independently built and documented within its own folder ([`Project-1`](./Project-1), [`Project-2`](./Project-2), [`Project-3`](./Project-3)).
- Product usage evidence frameworks are organized within each relevant project folder.
- **Product usage evidence is currently being collected and will be added as genuine OCI demonstrations are completed.**
- No credentials, API keys, private keys, or sensitive OCI information are included in this repository.

---

## 👨‍💻 About Me

- **Name:** Vigneshraj
- **GitHub:** [https://github.com/vignesh3003](https://github.com/vignesh3003)
- **Role:** Computer Science & Engineering student specializing in AI/ML & Software Engineering, currently participating in the Oracle ACE Apprentice Program.

---

## 📁 Repository Structure

```text
Oracle_ace_apprenticeship/
│
├── Project-1/
│   ├── src/
│   ├── docs/
│   │   ├── EVIDENCE_INDEX.md
│   │   ├── EVIDENCE_LOG.md
│   │   ├── architecture.md
│   │   └── oci_setup_guide.md
│   ├── evidence/
│   │   ├── API/
│   │   ├── DATABASE/
│   │   ├── OBJECT-STORAGE/
│   │   ├── OCI/
│   │   └── VISION-AI/
│   ├── ACE_SUBMISSION.md
│   ├── LICENSE
│   ├── README.md
│   ├── docker-compose.yml
│   └── .env.example
│
├── Project-2/
│   ├── src/
│   ├── docs/
│   │   ├── EVIDENCE_INDEX.md
│   │   ├── EVIDENCE_LOG.md
│   │   ├── api-gateway-setup.md
│   │   └── soda-configuration.md
│   ├── evidence/
│   │   ├── API-GATEWAY/
│   │   ├── DATABASE/
│   │   ├── FUNCTIONS/
│   │   ├── LANGUAGE-AI/
│   │   └── OCI/
│   ├── ACE_SUBMISSION.md
│   ├── LICENSE
│   ├── README.md
│   ├── docker-compose.yml
│   └── .env.example
│
├── Project-3/
│   ├── src/
│   ├── docs/
│   │   ├── EVIDENCE_INDEX.md
│   │   ├── EVIDENCE_LOG.md
│   │   ├── deployment-guide.md
│   │   └── oci-ons-setup.md
│   ├── evidence/
│   │   ├── ALERTING/
│   │   ├── COMPUTE/
│   │   ├── DATABASE/
│   │   └── OCI/
│   ├── ACE_SUBMISSION.md
│   ├── LICENSE
│   ├── README.md
│   ├── docker-compose.yml
│   └── .env.example
│
└── README.md
```

---

## 🚀 Projects

| Project | Description | Oracle Technologies | Status |
|:---|:---|:---|:---:|
| [**Project-1**](./Project-1) | **OracleDocuAI:** Full-stack document intelligence & vector search hub extracting OCR text from PDFs via OCI Vision AI and querying 384-dim vector embeddings in Oracle Database 23ai using native `VECTOR_DISTANCE(..., COSINE)`. | Oracle Autonomous Database 23ai, OCI Vision AI, OCI Object Storage, `python-oracledb` | **Completed** |
| [**Project-2**](./Project-2) | **Serverless Feedback Pulse:** Event-driven serverless sentiment analytics pipeline processing customer reviews through OCI Language AI for sentiment scores & keyphrases, storing JSON payloads in Oracle Autonomous JSON Database via SODA REST APIs. | OCI Functions (Fn Project), OCI API Gateway, OCI Language AI Service, Oracle Autonomous JSON Database (SODA REST) | **Completed** |
| [**Project-3**](./Project-3) | **OracleTelemetryX:** Edge-to-cloud infrastructure monitoring platform hosted on OCI Ampere Compute ARM. Ingests metrics via `python-oracledb` SessionPool connection pooling, executes statistical Z-score anomaly detection, and dispatches alerts via OCI Notification Service (ONS). | OCI Compute (Ampere A1 Flex ARM64), Oracle Autonomous Database (Connection Pooling), OCI Notification Service (ONS) | **Completed** |

---

## 🏗️ Oracle Technologies Used

- **Oracle Autonomous Database 23ai:** Utilized in [Project-1](./Project-1) for native `VECTOR(384, FLOAT32)` columns, in-memory neighbor graph indexes, and `VECTOR_DISTANCE` cosine similarity queries.
- **OCI Vision AI Service:** Utilized in [Project-1](./Project-1) via Python OCI SDK `AIServiceVisionClient` for document text detection (OCR) and line confidence scoring.
- **OCI Object Storage:** Utilized in [Project-1](./Project-1) as the durable bucket repository for uploaded raw PDF and image document assets.
- **OCI Functions (Fn Project):** Utilized in [Project-2](./Project-2) for serverless Python code execution handling review processing events on demand.
- **OCI API Gateway:** Utilized in [Project-2](./Project-2) for public HTTP REST routing (`/v1/feedback`) to serverless function handlers.
- **OCI Language AI Service:** Utilized in [Project-2](./Project-2) via Python OCI SDK for batch sentiment detection (Positive/Negative/Neutral) and keyphrase token extraction.
- **Oracle Autonomous JSON Database (SODA REST):** Utilized in [Project-2](./Project-2) for schemaless JSON document storage using Simple Oracle Document Access (SODA) HTTP REST endpoints.
- **OCI Compute (Ampere ARM):** Utilized in [Project-3](./Project-3) for hosting backend ingestion daemons and Docker containers on Always Free Ampere A1 Flex ARM64 VMs.
- **Oracle Database Connection Pooling (`python-oracledb` SessionPool):** Utilized in [Project-3](./Project-3) for low-latency concurrent time-series metric ingestion into Oracle Autonomous DB.
- **OCI Notification Service (ONS):** Utilized in [Project-3](./Project-3) via Python OCI SDK `NotificationDataPlaneClient` to publish instant email alert messages when metric anomalies cross statistical thresholds.

---

## 📸 Product Usage Evidence

Each project contains a dedicated `evidence/` directory structured by service component:

- **Project 1 Evidence Folders:** `evidence/OCI/`, `evidence/DATABASE/`, `evidence/OBJECT-STORAGE/`, `evidence/VISION-AI/`, `evidence/API/`
- **Project 2 Evidence Folders:** `evidence/OCI/`, `evidence/DATABASE/`, `evidence/FUNCTIONS/`, `evidence/API-GATEWAY/`, `evidence/LANGUAGE-AI/`
- **Project 3 Evidence Folders:** `evidence/OCI/`, `evidence/DATABASE/`, `evidence/COMPUTE/`, `evidence/ALERTING/`

> **Evidence Status Note:** Product usage evidence is currently being collected and will be added as genuine OCI demonstrations are completed.

Refer to `docs/EVIDENCE_INDEX.md` and `docs/EVIDENCE_LOG.md` inside each project folder for the complete checklist of required console screens and log verification records.

---

## 🔐 Security

- **No OCI Credentials:** Zero tenancy OCIDs, user OCIDs, compartment IDs, or database passwords are committed.
- **No Private Keys:** No API signing keys (`.pem`) or Oracle Database Wallet files (`cwallet.sso`) are included.
- **Strict Git Ignore:** All `.env` files are globally ignored by Git.
- **Placeholder Configs:** `.env.example` files contain empty/demo placeholder values only.
- **Safe Repositories:** Sensitive credentials must never be uploaded or committed.

---

## 🛠️ Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/vignesh3003/Oracle_ace_apprenticeship.git
   cd Oracle_ace_apprenticeship
   ```
2. Navigate to the desired project directory:
   ```bash
   cd Project-1   # or Project-2 / Project-3
   ```
3. Read the project's individual `README.md` for specific execution steps.
4. Copy `.env.example` to `.env` and configure environment variables.
5. Launch the application using Docker Compose or standalone shell scripts (`run.sh`).

---

## 📚 Documentation

Detailed documentation files are available in each project:

- **Project-1:**
  - [`Project-1/README.md`](./Project-1/README.md): Overview & Setup
  - [`Project-1/ACE_SUBMISSION.md`](./Project-1/ACE_SUBMISSION.md): Milestone Submission Document
  - [`Project-1/docs/architecture.md`](./Project-1/docs/architecture.md): Component Architecture & Sequence Flow
  - [`Project-1/docs/oci_setup_guide.md`](./Project-1/docs/oci_setup_guide.md): OCI Autonomous DB 23ai & Object Storage Setup
  - [`Project-1/docs/EVIDENCE_INDEX.md`](./Project-1/docs/EVIDENCE_INDEX.md): Screenshot Verification Index
  - [`Project-1/docs/EVIDENCE_LOG.md`](./Project-1/docs/EVIDENCE_LOG.md): Product Usage Audit Log
- **Project-2:**
  - [`Project-2/README.md`](./Project-2/README.md): Overview & Setup
  - [`Project-2/ACE_SUBMISSION.md`](./Project-2/ACE_SUBMISSION.md): Milestone Submission Document
  - [`Project-2/docs/api-gateway-setup.md`](./Project-2/docs/api-gateway-setup.md): OCI API Gateway Setup Guide
  - [`Project-2/docs/soda-configuration.md`](./Project-2/docs/soda-configuration.md): Oracle SODA REST Setup Guide
  - [`Project-2/docs/EVIDENCE_INDEX.md`](./Project-2/docs/EVIDENCE_INDEX.md): Screenshot Verification Index
  - [`Project-2/docs/EVIDENCE_LOG.md`](./Project-2/docs/EVIDENCE_LOG.md): Product Usage Audit Log
- **Project-3:**
  - [`Project-3/README.md`](./Project-3/README.md): Overview & Setup
  - [`Project-3/ACE_SUBMISSION.md`](./Project-3/ACE_SUBMISSION.md): Milestone Submission Document
  - [`Project-3/docs/deployment-guide.md`](./Project-3/docs/deployment-guide.md): OCI Ampere ARM Compute Deployment Guide
  - [`Project-3/docs/oci-ons-setup.md`](./Project-3/docs/oci-ons-setup.md): OCI Notification Service Setup Guide
  - [`Project-3/docs/EVIDENCE_INDEX.md`](./Project-3/docs/EVIDENCE_INDEX.md): Screenshot Verification Index
  - [`Project-3/docs/EVIDENCE_LOG.md`](./Project-3/docs/EVIDENCE_LOG.md): Product Usage Audit Log

---

## 🎯 Oracle ACE Apprentice Journey

These projects were developed as hands-on contributions after being accepted into the **Oracle ACE Apprentice Program**. They reflect genuine practical learning, software engineering implementation, and cloud-native architecture design using Oracle technologies.

---

## ⚠️ Important Notes

- All projects are independently developed, containerized, and documented.
- Oracle account credentials and API keys are never included.
- Users must configure their own OCI tenancy environment and credentials to reproduce live cloud deployments.
- Product usage evidence logs are structured to ensure authentic, non-fabricated Oracle Cloud interactions.

---

## 📄 License

Each project includes an open-source MIT License:
- [`Project-1/LICENSE`](./Project-1/LICENSE)
- [`Project-2/LICENSE`](./Project-2/LICENSE)
- [`Project-3/LICENSE`](./Project-3/LICENSE)
