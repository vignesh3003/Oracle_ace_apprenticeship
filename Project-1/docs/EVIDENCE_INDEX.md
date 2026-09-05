# Evidence Index — Project 1: OracleDocuAI

| ID | Evidence Title | Oracle Product | What It Demonstrates | Target Screenshot File | Status |
|---|---|---|---|---|---|
| **E01** | Autonomous Database Console | Oracle Autonomous DB 23ai | Database instance deployment, workload type (Transaction Processing), status (AVAILABLE), & Always Free designation | `evidence/OCI/01-adb-details-23ai.png` | Pending User Capture |
| **E02** | 23ai Vector Search Query | Oracle Database 23ai | Native SQL execution of `VECTOR_DISTANCE(embedding, :query_vec, COSINE)` in SQL Developer Web / Database Actions | `evidence/DATABASE/02-vector-distance-query.png` | Pending User Capture |
| **E03** | OCI Object Storage Bucket | OCI Object Storage | Bucket creation (`docu-ai-bucket`) and uploaded PDF/Image raw document assets | `evidence/OBJECT-STORAGE/03-bucket-documents.png` | Pending User Capture |
| **E04** | OCI Vision AI Service Metrics | OCI Vision AI Service | Document text detection (OCR) API call volume graphs and low-latency response metrics | `evidence/VISION-AI/04-vision-ocr-metrics.png` | Pending User Capture |
| **E05** | FastAPI Swagger API Interactivity | OCI SDK & python-oracledb | Successful HTTP 201 Created response from `/api/v1/documents/upload` and `/api/v1/search` endpoints | `evidence/API/05-fastapi-swagger-upload.png` | Pending User Capture |

---

## Detailed Capture Guidance for Submission Evidence

### Screenshot E01: Autonomous Database Console Details
- **Oracle Service:** Oracle Autonomous Database 23ai
- **Location in OCI Console:** Oracle Database $\rightarrow$ Autonomous Database $\rightarrow$ Click `DocuAI23DB`
- **What Must Be Visible:**
  - Database Name: `DocuAI23DB`
  - Lifecycle State: `AVAILABLE` (Green badge)
  - Workload Type: `Transaction Processing`
  - Database Version: `23ai`
  - Always Free badge (if using Always Free tier)
- **Save As:** `PROJECT-1/evidence/OCI/01-adb-details-23ai.png`

### Screenshot E02: Vector Search SQL Query Execution
- **Oracle Service:** Oracle Database 23ai (Database Actions / SQL Developer Web)
- **Location:** OCI Console $\rightarrow$ Autonomous DB Details $\rightarrow$ Database Actions $\rightarrow$ SQL
- **Action to Perform:** Run the following SQL query against your database:
  ```sql
  SELECT chunk_id, document_id, VECTOR_DISTANCE(embedding, :query_vec, COSINE) AS distance
  FROM document_chunks
  ORDER BY distance ASC;
  ```
- **What Must Be Visible:**
  - The SQL Worksheet containing the `VECTOR_DISTANCE` query.
  - The Query Result grid displaying returned vector distances and similarity percentages.
- **Save As:** `PROJECT-1/evidence/DATABASE/02-vector-distance-query.png`

### Screenshot E03: OCI Object Storage Bucket Assets
- **Oracle Service:** OCI Object Storage
- **Location in OCI Console:** Storage $\rightarrow$ Buckets $\rightarrow$ `docu-ai-bucket`
- **What Must Be Visible:**
  - Bucket Name: `docu-ai-bucket`
  - Compartment name
  - List of uploaded document objects (e.g. `doc_xxx_report.pdf`)
- **Save As:** `PROJECT-1/evidence/OBJECT-STORAGE/03-bucket-documents.png`

### Screenshot E04: OCI Vision AI Service Telemetry
- **Oracle Service:** OCI Vision AI Service
- **Location in OCI Console:** Analytics & AI $\rightarrow$ Vision $\rightarrow$ Metrics / Request History
- **What Must Be Visible:**
  - Request volume graphs showing `AnalyzeDocument` API invocations.
- **Save As:** `PROJECT-1/evidence/VISION-AI/04-vision-ocr-metrics.png`

### Screenshot E05: Application API Vector Search Results
- **Oracle Service:** Application Client / FastAPI Swagger
- **Location:** `http://localhost:8000/docs` or Next.js Dashboard (`http://localhost:3000`)
- **What Must Be Visible:**
  - Successful vector search result displaying Cosine Similarity scores.
- **Save As:** `PROJECT-1/evidence/API/05-fastapi-swagger-upload.png`
