# Oracle ACE Apprentice Contribution Document

# Contribution Title
**Serverless Feedback Pulse: Event-Driven Microservice Sentiment Analytics Pipeline using OCI Functions & SODA REST DB**

# Project Overview
Serverless Feedback Pulse is an event-driven serverless text analytics pipeline built on OCI API Gateway, OCI Functions (Fn Project), OCI Language AI, and Oracle Autonomous JSON Database (SODA REST API).

# Problem Statement
SaaS platforms and digital products process thousands of customer reviews daily. Managing dedicated servers for spike-heavy text analytics workloads is costly, while relational schemas make storing evolving JSON metadata inflexible.

# Solution
The application exposes public REST routes via OCI API Gateway, executes on-demand microservices inside OCI Functions containers, calls OCI Language AI Service for sentiment scores and keyphrase extraction, and persists schemaless JSON payloads into Oracle Autonomous JSON Database using SODA.

# Oracle Technologies Used

### 1. OCI Functions (Fn Project Serverless Engine)
- **What it does:** Runs stateless Python serverless code triggered on demand.
- **Why it was selected:** Zero server maintenance, sub-second container cold start times, and native OCI Resource Principal authentication.
- **How it was integrated:** Created Fn function container deployed to OCI Container Registry (OCIR).

### 2. OCI API Gateway
- **What it does:** Routes public HTTP REST traffic to serverless functions securely.
- **Why it was selected:** Low latency API management with built-in rate limiting and OCI IAM authorization.
- **How it was integrated:** Defined API deployment routes pointing `/v1/feedback` to the OCI Function handler.

### 3. OCI Language AI Service
- **What it does:** Extracts sentiment (Positive/Negative/Neutral) and keyphrase tokens.
- **Why it was selected:** Production-grade NLP exposed via Python OCI SDK.
- **How it was integrated:** Invoked `oci.ai_language.AIServiceLanguageClient.batch_detect_language_sentiments`.

### 4. Oracle Autonomous JSON Database (SODA REST API)
- **What it does:** Stores non-relational JSON document collections.
- **Why it was selected:** Schema-agnostic JSON storage with native SQL indexing and ORDS SODA REST support.
- **How it was integrated:** HTTP POST requests to ORDS SODA endpoint (`/ords/admin/soda/latest/feedback_collection`).

# My Implementation
1. Authored Python Fn serverless handler (`func.py`) integrating `oci.ai_language` SDK and SODA REST client.
2. Created cURL initialization scripts (`scripts/soda_bootstrap.sh`) to provision SODA JSON collections via ORDS.
3. Configured OCI API Gateway deployments and mapped CORS headers for web client routing.
4. Built a React dashboard leveraging Recharts to render sentiment charts and keyphrase clouds.

# Architecture

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

# Key Features
1. **Serverless Execution:** Runs on-demand without managing server instances.
2. **Multilingual AI Sentiment Analysis:** Classifies reviews as Positive, Negative, or Neutral.
3. **Automatic Keyphrase Extraction:** Identifies key subject tokens.
4. **Schemaless Document Storage:** Persists JSON objects via SODA REST.
5. **Real-time Visual Analytics:** React dashboard showing live sentiment distributions.

# Technical Challenges & Solutions

| Challenge | Solution |
| :--- | :--- |
| **Connecting OCI Functions to SODA DB without local SQL drivers** | Utilized Oracle REST Data Services (ORDS) SODA REST API for pure HTTPS JSON insertion. |
| **Authenticating serverless functions securely** | Configured OCI Resource Principals, eliminating hardcoded API keys in function code. |

# Product Usage Evidence To Capture
1. **OCI Console - OCI Functions Details Page:** Showing active `analyze-feedback` function.
2. **OCI Console - OCI API Gateway Deployments:** Screenshot showing active HTTP route `/v1/feedback`.
3. **OCI Console - OCI Language AI Metrics:** Service request graphs showing API call volume.
4. **Oracle Database Actions (SODA Viewer):** Screenshot displaying JSON documents stored inside `feedback_collection`.

# GitHub Repository
`https://github.com/your-username/serverless-feedback-pulse`
