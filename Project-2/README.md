# Serverless Feedback Pulse: Microservice Sentiment Analytics Pipeline

[![OCI Functions](https://img.shields.io/badge/OCI-Functions-orange.svg)](https://www.oracle.com/cloud/cloud-native/functions/)
[![OCI Language AI](https://img.shields.io/badge/OCI-Language%20AI-red.svg)](https://www.oracle.com/artificial-intelligence/language/)
[![Oracle SODA DB](https://img.shields.io/badge/Oracle-SODA%20JSON%20DB-blue.svg)](https://www.oracle.com/database/sqldeveloper/docs/soda.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An event-driven serverless sentiment analysis pipeline using **OCI API Gateway**, **OCI Functions (Fn Project)**, **OCI Language AI Service**, and **Oracle Autonomous JSON Database (SODA REST API)**.

---

## Problem Statement
High-volume customer review processing requires immediate sentiment categorization without incurring costs for idle servers. Relational table structures also force fixed schemas on unstructured feedback.

---

## Solution
This microservice processes incoming feedback through OCI API Gateway, triggers serverless Python code on OCI Functions, extracts sentiment and keyphrases using OCI Language AI, and persists non-relational JSON documents directly into Oracle Autonomous JSON Database using SODA.

---

## Architecture

```text
User Client (React Sentiment Dashboard)
       │
       ▼
OCI API Gateway (Public Route: /v1/feedback)
       │
       ▼
OCI Function (Fn Project Python Container)
       ├───► OCI Language AI Service (Sentiment & Keyphrases)
       └───► Oracle Autonomous JSON Database (SODA REST Endpoint)
```

---

## Oracle Technologies Used
- **OCI Functions:** Serverless Python execution engine running Fn Project containers.
- **OCI API Gateway:** Manages public REST routing and rate limiting.
- **OCI Language AI:** AI service performing sentiment classification and keyphrase extraction.
- **Oracle Autonomous JSON Database:** Stores schemaless JSON document collections via SODA REST APIs.

---

## Features
- ⚡ **Zero-Server Infrastructure:** Serverless architecture powered by OCI Functions.
- 🎯 **Multilingual AI Sentiment Analysis:** Classifies reviews into Positive, Neutral, or Negative.
- 🏷️ **Automatic Keyphrase Extraction:** Highlights critical product keywords.
- 📦 **Schemaless Document Access:** SODA REST API storage without SQL schema management.
- 📊 **React Telemetry Dashboard:** Visualizes sentiment metrics via Recharts.

---

## Installation & Running

### 1. Run Backend API Proxy
```bash
cd backend_api
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### 2. Run React Dashboard
```bash
cd dashboard
npm install
npm run dev
```

Dashboard runs on `http://localhost:3000`.

---

## Screenshots / Evidence
- **OCI Console Functions Details** (`docs/screenshots/oci_functions.png`)
- **OCI API Gateway Routes** (`docs/screenshots/oci_api_gateway.png`)
- **Oracle SODA Collection Document Viewer** (`docs/screenshots/soda_documents.png`)
- **React Telemetry Dashboard** (`docs/screenshots/dashboard.png`)

---

## License
[MIT License](LICENSE)
