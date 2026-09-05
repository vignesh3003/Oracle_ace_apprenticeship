# Oracle ACE Apprentice Contribution Document

# Contribution Title
**OracleDocuAI: Enterprise Document Intelligence & Semantic Vector Search System powered by Oracle Database 23ai & OCI Vision AI**

# Project Overview
OracleDocuAI is a full-stack, cloud-native document intelligence platform designed to extract unstructured text from PDFs and scanned images using OCI Vision AI, convert extracted text into 384-dimensional vector embeddings, and store them natively in Oracle Autonomous Database 23ai using `VECTOR` data types for cosine similarity semantic retrieval.

# Problem Statement
Organizations routinely store millions of unstructured PDF reports, legal contracts, and scanned receipts in object storage. Traditional keyword searches fail when user queries do not match exact wording, and standard relational databases cannot execute vector distance math natively.

# Solution
OracleDocuAI solves this by combining OCI Object Storage for file persistence, OCI Vision AI for optical character recognition (OCR), and Oracle Autonomous Database 23ai for native AI Vector Search. Users perform natural language searches against document chunks with instant sub-second vector similarity scoring.

# Oracle Technologies Used

### 1. Oracle Autonomous Database 23ai (Transaction Processing)
- **What it does:** Serves as the primary transactional and vector database.
- **Why it was selected:** Oracle 23ai introduces native `VECTOR` data types and `VECTOR_DISTANCE` functions directly inside the SQL engine.
- **How it was integrated:** Interfaced using the official `python-oracledb` driver. Created tables with `VECTOR(384, FLOAT32)` columns and executed SQL queries using `VECTOR_DISTANCE(c.embedding, :query_vec, COSINE)`.

### 2. OCI Vision AI Service
- **What it does:** Extracts text (OCR), document structure, and lines from scanned files.
- **Why it was selected:** High-accuracy document text detection exposed via REST APIs and official Python OCI SDK.
- **How it was integrated:** Invoked `oci.ai_vision.AIServiceVisionClient.analyze_document` via Python SDK.

### 3. OCI Object Storage
- **What it does:** Provides durable object bucket storage for raw documents.
- **Why it was selected:** OCI Always Free Tier provides 10 GB of durable Object Storage.
- **How it was integrated:** Uploaded files via `oci.object_storage.ObjectStorageClient.put_object`.

# My Implementation
I personally designed, developed, and tested the complete system architecture:
1. Engineered the FastAPI backend implementing Python `oci` SDK authentication and `python-oracledb` connection pooling.
2. Formulated Oracle 23ai DDL SQL scripts introducing `VECTOR(384, FLOAT32)` columns and cosine in-memory vector indexes.
3. Implemented a dual execution engine supporting both live OCI cloud connections and a zero-dependency local simulation mode.
4. Built a responsive Next.js 14 dashboard using Tailwind CSS and TypeScript to visualize OCR metrics and vector similarity scores.

# Architecture

```text
User / Client Browser (Next.js 14 Dashboard)
       │
       ▼
FastAPI Backend API (Python 3.11 + python-oracledb + OCI SDK)
       ├───► OCI Object Storage (PDF / Image Upload Bucket)
       ├───► OCI Vision AI Service (AnalyzeDocument OCR API)
       └───► Oracle Autonomous Database 23ai (VECTOR(384, FLOAT32) + VECTOR_DISTANCE)
```

# Key Features
1. **Multimodal Ingestion:** Uploads PDFs/images directly to OCI Object Storage.
2. **Automated OCR:** Invokes OCI Vision AI API to convert image pixels to structured text.
3. **Native 23ai Vector Indexing:** Generates 384-dimensional embeddings and stores them in Oracle 23ai `VECTOR` columns.
4. **Cosine Similarity Search:** Executes native `VECTOR_DISTANCE(..., COSINE)` SQL queries.
5. **Interactive UI:** Next.js dashboard featuring document catalogs and live similarity score badges.

# Technical Challenges & Solutions

| Challenge | Solution |
| :--- | :--- |
| **Connecting Python to Oracle ADB 23ai without local Oracle Client binaries** | Configured `python-oracledb` in Thin Mode, utilizing pure Python TLS communication with Database Wallet files. |
| **Executing Vector Search without expensive third-party vector DBs** | Utilized Oracle Database 23ai's native `VECTOR` data type, eliminating external vector database dependencies. |
| **Ensuring offline local development compatibility** | Implemented a dual-mode system architecture with automated mock fallbacks for OCI SDK calls. |

# What I Learned
- Configuring OCI IAM policies and API key authentication.
- Implementing Oracle Autonomous Database 23ai AI Vector Search syntax.
- Optimizing Python FastAPI database connection pooling with `python-oracledb`.
- Managing OCI Object Storage bucket life cycles and OCI Vision AI API calls.

# Product Usage Evidence To Capture
1. **OCI Console - Autonomous Database Details Page:** Displaying ADB 23ai instance name (`DocuAI23DB`) and Always Free badge.
2. **OCI Console - Object Storage Bucket Page:** Showing uploaded PDF objects in `docu-ai-bucket`.
3. **OCI Console - OCI Vision AI Service Metrics:** Screenshot of request count graphs in OCI Console.
4. **Oracle Database Actions / SQL Developer Web:** Screen capture executing `SELECT VECTOR_DISTANCE(...) FROM document_chunks`.
5. **Terminal Logs:** Server logs demonstrating successful `python-oracledb` connection and OCI SDK calls.

# GitHub Repository
`https://github.com/your-username/oracledocu-ai`
