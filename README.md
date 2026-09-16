# Oracle ACE Apprentice – Product Usage Milestone Contributions

This repository contains my hands-on Oracle technology projects created for my **Oracle ACE Apprentice** journey. The projects demonstrate genuine Oracle product usage across cloud infrastructure, autonomous databases, AI services, generative AI, serverless architectures, and security vault services.

- Each project is independently built and documented within its own folder ([`Project-1`](./Project-1), [`Project-2`](./Project-2), [`Project-3`](./Project-3), [`Project-4`](./Project-4), [`Project-5`](./Project-5), [`Project-6`](./Project-6)).
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
├── Project-1/   # OracleDocuAI (23ai Vector Search + OCI Vision AI)
├── Project-2/   # Serverless Feedback Pulse (OCI Functions + OCI Language + SODA DB)
├── Project-3/   # OracleTelemetryX (OCI Ampere ARM + ONS Alerting + DB SessionPool)
├── Project-4/   # OracleGenAI-RAG (OCI Generative AI Cohere/Llama + Autonomous DB)
├── Project-5/   # OCI MediaStream-AI (OCI Speech AI Service + Object Storage)
├── Project-6/   # OracleCloudGuard-X (OCI Vault KMS Security Auditor)
└── README.md
```

---

## 🚀 Projects

| Project | Description | Oracle Technologies | Status |
|:---|:---|:---|:---:|
| [**Project-1**](./Project-1) | **OracleDocuAI:** Full-stack document intelligence & vector search hub extracting OCR text from PDFs via OCI Vision AI and querying 384-dim vector embeddings in Oracle Database 23ai using native `VECTOR_DISTANCE(..., COSINE)`. | Oracle Autonomous Database 23ai, OCI Vision AI, OCI Object Storage, `python-oracledb` | **Completed** |
| [**Project-2**](./Project-2) | **Serverless Feedback Pulse:** Event-driven serverless sentiment analytics pipeline processing customer reviews through OCI Language AI for sentiment scores & keyphrases, storing JSON payloads in Oracle Autonomous JSON Database via SODA REST APIs. | OCI Functions (Fn Project), OCI API Gateway, OCI Language AI Service, Oracle Autonomous JSON Database (SODA REST) | **Completed** |
| [**Project-3**](./Project-3) | **OracleTelemetryX:** Edge-to-cloud infrastructure monitoring platform hosted on OCI Ampere Compute ARM. Ingests metrics via `python-oracledb` SessionPool connection pooling, executes statistical Z-score anomaly detection, and dispatches alerts via OCI Notification Service (ONS). | OCI Compute (Ampere A1 Flex ARM64), Oracle Autonomous Database (Connection Pooling), OCI Notification Service (ONS) | **Completed** |
| [**Project-4**](./Project-4) | **OracleGenAI-RAG:** Enterprise knowledge assistant leveraging OCI Generative AI Service (Cohere Command R+ / Meta Llama 3 models) via Python OCI SDK, persisting chat conversation history in Oracle Autonomous Database. | OCI Generative AI Service, Oracle Autonomous Database, OCI Object Storage | **Completed** |
| [**Project-5**](./Project-5) | **OCI MediaStream-AI:** Multimodal media transcriber ingesting audio/video streams into OCI Object Storage, invoking OCI Speech AI API for automatic speech-to-text transcription, and indexing transcripts in Oracle Autonomous Database. | OCI Speech AI Service, OCI Object Storage, Oracle Autonomous Database | **Completed** |
| [**Project-6**](./Project-6) | **OracleCloudGuard-X:** Automated infrastructure security compliance auditor verifying AES-256 secret encryption inside OCI Vault (KMS), checking VCN ingress security policies, and recording compliance logs in Oracle Autonomous Database. | OCI Vault (Key Management Service), OCI Notification Service (ONS), Oracle Autonomous Database | **Completed** |

---

## 🏗️ Oracle Technologies Used

- **Oracle Autonomous Database 23ai:** Utilized in Project-1 for native `VECTOR(384, FLOAT32)` columns and `VECTOR_DISTANCE` cosine similarity queries.
- **OCI Vision AI Service:** Utilized in Project-1 for document text detection (OCR) and line confidence scoring.
- **OCI Object Storage:** Utilized in Project-1, Project-4, and Project-5 as durable bucket repositories for raw documents and audio streams.
- **OCI Functions (Fn Project):** Utilized in Project-2 for serverless Python code execution handling review processing events.
- **OCI API Gateway:** Utilized in Project-2 for public HTTP REST routing (`/v1/feedback`) to serverless function handlers.
- **OCI Language AI Service:** Utilized in Project-2 for batch sentiment detection and keyphrase token extraction.
- **Oracle Autonomous JSON Database (SODA REST):** Utilized in Project-2 for schemaless JSON document storage using SODA HTTP REST endpoints.
- **OCI Compute (Ampere ARM):** Utilized in Project-3 for hosting telemetry daemons and Docker containers on Always Free Ampere A1 Flex ARM64 VMs.
- **Oracle Database Connection Pooling (`python-oracledb` SessionPool):** Utilized in Project-3 for low-latency concurrent metric writes.
- **OCI Notification Service (ONS):** Utilized in Project-3 and Project-6 to publish instant email alerts when metric anomalies or security events occur.
- **OCI Generative AI Service:** Utilized in Project-4 via `oci.generative_ai_inference` SDK for Cohere Command R+ and Meta Llama 3 LLM chat inference.
- **OCI Speech AI Service:** Utilized in Project-5 via `oci.ai_speech` SDK for automatic speech-to-text transcription jobs.
- **OCI Vault (KMS):** Utilized in Project-6 via `oci.key_management` SDK for secret encryption and KMS key security auditing.

---

## 🔐 Security

- **No OCI Credentials:** Zero tenancy OCIDs, user OCIDs, compartment IDs, or database passwords are committed.
- **No Private Keys:** No API signing keys (`.pem`) or Oracle Database Wallet files (`cwallet.sso`) are included.
- **Strict Git Ignore:** All `.env` files are globally ignored by Git.
- **Placeholder Configs:** `.env.example` files contain empty/demo placeholder values only.

---

## 📄 License

Each project includes an open-source MIT License:
- [`Project-1/LICENSE`](./Project-1/LICENSE)
- [`Project-2/LICENSE`](./Project-2/LICENSE)
- [`Project-3/LICENSE`](./Project-3/LICENSE)
- [`Project-4/LICENSE`](./Project-4/LICENSE)
- [`Project-5/LICENSE`](./Project-5/LICENSE)
- [`Project-6/LICENSE`](./Project-6/LICENSE)
