# Evidence Index — Project 2: Serverless Feedback Pulse

| ID | Evidence Title | Oracle Product | What It Demonstrates | Target Screenshot File | Status |
|---|---|---|---|---|---|
| **E01** | OCI Functions Details | OCI Functions (Fn Project) | Deployed Python serverless function (`analyze-feedback`) in OCI Container Registry (OCIR) | `evidence/FUNCTIONS/01-function-deployed.png` | Pending User Capture |
| **E02** | OCI API Gateway Deployment | OCI API Gateway | Active HTTP REST route (`/v1/feedback`) pointing to OCI Function handler | `evidence/API-GATEWAY/02-api-gateway-deployment.png` | Pending User Capture |
| **E03** | OCI Language AI Metrics | OCI Language AI Service | Sentiment classification & keyphrase extraction request telemetry graphs | `evidence/LANGUAGE-AI/03-language-ai-metrics.png` | Pending User Capture |
| **E04** | SODA JSON Document Collection | Oracle Autonomous JSON DB | Stored non-relational JSON document payloads in `feedback_collection` via SODA REST API | `evidence/DATABASE/04-soda-json-documents.png` | Pending User Capture |
| **E05** | React Dashboard Analytics | Full-Stack Integration | Live React sentiment pie chart and extracted keyphrase cloud UI | `evidence/OCI/05-react-dashboard-live.png` | Pending User Capture |

---

## Detailed Capture Guidance for Submission Evidence

### Screenshot E01: OCI Functions Deployment
- **Oracle Service:** OCI Functions
- **Location in OCI Console:** Developer Services $\rightarrow$ Functions $\rightarrow$ Applications $\rightarrow$ `feedback-app`
- **What Must Be Visible:**
  - Function Name: `analyze-feedback`
  - Runtime: `Python`
  - Memory: `256 MB`
  - Invocation Metrics / Logs
- **Save As:** `PROJECT-2/evidence/FUNCTIONS/01-function-deployed.png`

### Screenshot E02: OCI API Gateway Routes
- **Oracle Service:** OCI API Gateway
- **Location in OCI Console:** Developer Services $\rightarrow$ API Gateway $\rightarrow$ Gateways $\rightarrow$ `feedback-gateway` $\rightarrow$ Deployments
- **What Must Be Visible:**
  - Path Prefix: `/v1`
  - Route: `/feedback` (HTTP POST)
  - Backend Type: `OCI Functions` (`analyze-feedback`)
- **Save As:** `PROJECT-2/evidence/API-GATEWAY/02-api-gateway-deployment.png`

### Screenshot E03: OCI Language AI Service Telemetry
- **Oracle Service:** OCI Language AI Service
- **Location in OCI Console:** Analytics & AI $\rightarrow$ Language $\rightarrow$ Batch Sentiment / Keyphrase Metrics
- **What Must Be Visible:**
  - Request volume graphs showing sentiment and keyphrase detection API calls.
- **Save As:** `PROJECT-2/evidence/LANGUAGE-AI/03-language-ai-metrics.png`

### Screenshot E04: SODA JSON Collection in Database Actions
- **Oracle Service:** Oracle Autonomous JSON Database (SODA REST)
- **Location in OCI Console:** Autonomous DB Details $\rightarrow$ Database Actions $\rightarrow$ JSON / SODA Viewer
- **What Must Be Visible:**
  - Collection Name: `feedback_collection`
  - JSON document content showing `"sentiment": "Positive"`, `"keyphrases": [...]`, `"customer_id": "..."`.
- **Save As:** `PROJECT-2/evidence/DATABASE/04-soda-json-documents.png`

### Screenshot E05: React Dashboard Visualization
- **Oracle Service:** Full Application Client
- **Location:** `http://localhost:3000`
- **What Must Be Visible:**
  - Live React dashboard displaying sentiment distribution chart and keyphrase tags.
- **Save As:** `PROJECT-2/evidence/OCI/05-react-dashboard-live.png`
