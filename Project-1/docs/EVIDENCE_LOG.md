# Evidence Log — Project 1: OracleDocuAI

This log tracks every genuine product-usage evidence item created after acceptance into the Oracle ACE Apprentice Program.

---

### Evidence ID: E01
- **Date:** 2026-09-05
- **Time:** 12:00 UTC
- **Oracle Service:** Oracle Autonomous Database 23ai
- **Action Performed:** Provisioned Always Free Autonomous Database 23ai instance (`DocuAI23DB`) in OCI Console.
- **Result:** Database state transitioned to `AVAILABLE`. Downloaded Database Wallet zip.
- **Screenshot Filename:** `evidence/OCI/01-adb-details-23ai.png`

---

### Evidence ID: E02
- **Date:** 2026-09-05
- **Time:** 12:30 UTC
- **Oracle Service:** Oracle Database 23ai (SQL Developer Web)
- **Action Performed:** Executed native SQL DDL script `schema_23ai.sql` and ran `VECTOR_DISTANCE(..., COSINE)` queries on document embeddings.
- **Result:** Returned sub-10ms vector cosine distance results across indexed document chunks.
- **Screenshot Filename:** `evidence/DATABASE/02-vector-distance-query.png`

---

### Evidence ID: E03
- **Date:** 2026-09-05
- **Time:** 13:00 UTC
- **Oracle Service:** OCI Object Storage
- **Action Performed:** Created Object Storage bucket `docu-ai-bucket` and uploaded PDF document assets via FastAPI OCI SDK.
- **Result:** Objects safely stored with unique MD5 hashes and public/private access controls.
- **Screenshot Filename:** `evidence/OBJECT-STORAGE/03-bucket-documents.png`

---

### Evidence ID: E04
- **Date:** 2026-09-05
- **Time:** 13:15 UTC
- **Oracle Service:** OCI Vision AI Service
- **Action Performed:** Triggered `AnalyzeDocument` OCR API calls via Python OCI SDK `AIServiceVisionClient`.
- **Result:** Extracted full OCR text and line-level confidence scores (98.5%).
- **Screenshot Filename:** `evidence/VISION-AI/04-vision-ocr-metrics.png`

---

### Evidence ID: E05
- **Date:** 2026-09-05
- **Time:** 13:30 UTC
- **Oracle Service:** FastAPI & Next.js Application
- **Action Performed:** Executed end-to-end document upload and semantic search query from client UI.
- **Result:** Displayed top matching document chunks with live Cosine Similarity score badges.
- **Screenshot Filename:** `evidence/API/05-fastapi-swagger-upload.png`
