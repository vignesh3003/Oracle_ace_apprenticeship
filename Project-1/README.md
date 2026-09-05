# OracleDocuAI: Enterprise Document Intelligence & Semantic Vector Search System

[![Oracle Database 23ai](https://img.shields.io/badge/Oracle%20Database-23ai-red.svg)](https://www.oracle.com/database/23ai/)
[![OCI Vision AI](https://img.shields.io/badge/OCI-Vision%20AI-orange.svg)](https://www.oracle.com/artificial-intelligence/vision/)
[![Python FastAPI](https://img.shields.io/badge/FastAPI-0.109-emerald.svg)](https://fastapi.tiangolo.com/)
[![Next.js 14](https://img.shields.io/badge/Next.js-14.1-blue.svg)](https://nextjs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An open-source enterprise document processing and semantic vector search platform powered by **Oracle Autonomous Database 23ai** and **OCI Vision AI Service**. The system ingests unstructured PDFs and scanned document images, extracts text via OCI Vision OCR, generates 384-dimensional vector embeddings, and stores them in Oracle 23ai native `VECTOR` columns for cosine similarity search.

---

## Problem Statement
Organizations routinely store vast volumes of unstructured PDF reports, technical manuals, and scanned legal documents in cloud storage. Standard keyword search engines fail when user query phrasing differs from document wording, while traditional relational databases cannot execute vector distance calculations efficiently.

---

## Solution
OracleDocuAI integrates cloud-native object storage, computer vision OCR, and native database vector search into a single pipeline:
1. **Document Upload:** Ingests PDFs/Images directly to **OCI Object Storage**.
2. **AI Text Extraction:** Processes files through **OCI Vision AI `AnalyzeDocument` API**.
3. **Native Vector Search:** Index 384-dimensional vector embeddings into **Oracle Autonomous Database 23ai** and queries them using native `VECTOR_DISTANCE(..., COSINE)` SQL functions.

---

## Architecture

```text
User / Client Browser (Next.js 14 Dashboard)
       │
       ▼
FastAPI Backend API (Python 3.11 + python-oracledb + OCI SDK)
       ├───► OCI Object Storage (PDF / Image Upload Bucket)
       ├───► OCI Vision AI Service (AnalyzeDocument OCR API)
       └───► Oracle Autonomous Database 23ai (VECTOR(384, FLOAT32) + VECTOR_DISTANCE)
```

---

## Oracle Technologies Used
- **Oracle Autonomous Database 23ai:** Stores document metadata and 384-dimensional float vector embeddings using native `VECTOR` columns and in-memory vector neighbor graph indexes.
- **OCI Vision AI Service:** Performs document text detection (OCR) and structural document analysis via official Python OCI SDK.
- **OCI Object Storage:** Serves as the durable cloud bucket repository for raw document assets.
- **`python-oracledb`:** Official Oracle Python database driver operating in Thin Mode with TLS wallet authentication.

---

## Features
- 📄 **Multimodal Document Upload:** Supports PDF, PNG, JPG, JPEG files.
- 👁️ **Automated OCI Vision OCR:** High-precision text extraction with confidence scoring.
- 🧠 **Native 23ai Vector Indexing:** 384-dimensional vector embedding storage directly inside Oracle Database 23ai.
- 🔍 **Natural Language Semantic Search:** Sub-second vector search via `VECTOR_DISTANCE(..., COSINE)`.
- 💻 **Responsive SRE/Dev Dashboard:** Built with Next.js 14, Tailwind CSS, and TypeScript.
- ⚡ **Dual Execution Mode:** Runs out-of-the-box in local demo simulation mode AND live OCI Cloud mode.

---

## Installation

### Prerequisites
- Python 3.11+
- Node.js 18+
- Git

### Clone Repository
```bash
git clone https://github.com/your-username/oracledocu-ai.git
cd oracledocu-ai
```

---

## Configuration

Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

### Local Demo Mode (Default)
Keep `APP_ENV=development` in `.env`. The backend will automatically simulate OCI Vision and Oracle 23ai responses in-memory without needing active cloud keys.

### Real Oracle Cloud Mode
Update `.env` with your active OCI details:
```ini
APP_ENV=production
OCI_COMPARTMENT_ID=ocid1.compartment.oc1..aaaaaaaaxxx
OCI_BUCKET_NAME=docu-ai-bucket
ORACLE_DB_USER=admin
ORACLE_DB_PASSWORD=YourPassword23ai!
ORACLE_DB_DSN=docuai23db_high
ORACLE_DB_WALLET_LOCATION=./oracle_wallet
```

---

## Running Locally

### Option A: Running with Shell Scripts

1. **Start Backend Server (FastAPI):**
   ```bash
   cd backend
   chmod +x run.sh
   ./run.sh
   ```
   FastAPI server runs on `http://localhost:8000` (Swagger docs at `/docs`).

2. **Start Frontend Server (Next.js):**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
   Next.js dashboard runs on `http://localhost:3000`.

### Option B: Running with Docker Compose
```bash
docker-compose up --build
```

---

## Deployment

Deploying to an OCI Always Free Ampere A1 Compute Instance:
```bash
# SSH into OCI Ampere VM
ssh ubuntu@<your-oci-vm-public-ip>

# Clone repo & run with Docker Compose
git clone https://github.com/your-username/oracledocu-ai.git
cd oracledocu-ai
docker-compose up -d
```

---

## Screenshots / Product Usage Evidence
- **OCI Console Autonomous Database 23ai Details** (`docs/screenshots/oci_adb_details.png`)
- **OCI Object Storage Bucket** (`docs/screenshots/oci_bucket.png`)
- **OCI Vision AI Service Request Telemetry** (`docs/screenshots/oci_vision_metrics.png`)
- **Oracle Database Actions SQL Vector Query** (`docs/screenshots/oracle_sql_vector_query.png`)
- **Next.js Dashboard & Semantic Search** (`docs/screenshots/dashboard_vector_search.png`)

---

## Challenges and Solutions
- **Challenge:** Interfacing Python with Oracle ADB 23ai without heavy Oracle Instant Client binaries.
- **Solution:** Utilized `python-oracledb` in Thin Mode, allowing pure Python TLS wallet connections.
- **Challenge:** Handling high-dimensional vector math without external vector databases.
- **Solution:** Leveraged Oracle Database 23ai's native `VECTOR` data type and `VECTOR_DISTANCE` functions.

---

## Key Learnings
- Configuring OCI API signing keys and IAM compartment policies.
- Formulating Oracle Database 23ai DDL scripts with `VECTOR(384, FLOAT32)` columns.
- Building responsive Next.js 14 interfaces interfacing with FastAPI backends.

---

## Future Improvements
- Integrate Oracle 23ai `Select AI` feature to allow SQL natural language translation (`SELECT AI ask 'Show me all legal contracts'`).
- Add chunk highlighting inside original PDF files using PDF.js.

---

## Contributing
Pull requests are welcome! Please open an issue first to discuss intended changes.

---

## License
[MIT License](LICENSE)
