# Evidence Log — Project 2: Serverless Feedback Pulse

This log tracks every genuine product-usage evidence item created after acceptance into the Oracle ACE Apprentice Program.

---

### Evidence ID: E01
- **Date:** 2026-09-05
- **Time:** 14:00 UTC
- **Oracle Service:** OCI Functions (Fn Project)
- **Action Performed:** Deployed Fn Python container function `analyze-feedback` to OCI Container Registry (OCIR) via `fn deploy`.
- **Result:** Function registered in OCI Functions console under `feedback-app`.
- **Screenshot Filename:** `evidence/FUNCTIONS/01-function-deployed.png`

---

### Evidence ID: E02
- **Date:** 2026-09-05
- **Time:** 14:30 UTC
- **Oracle Service:** OCI API Gateway
- **Action Performed:** Created public API Gateway deployment routing POST `/v1/feedback` traffic to OCI Function handler.
- **Result:** Gateway endpoint published with low-latency HTTP route.
- **Screenshot Filename:** `evidence/API-GATEWAY/02-api-gateway-deployment.png`

---

### Evidence ID: E03
- **Date:** 2026-09-05
- **Time:** 15:00 UTC
- **Oracle Service:** OCI Language AI Service
- **Action Performed:** Executed `batch_detect_language_sentiments` and `batch_detect_language_key_phrases` API requests.
- **Result:** Extracted sentiment classification and keyphrase tokens for incoming review streams.
- **Screenshot Filename:** `evidence/LANGUAGE-AI/03-language-ai-metrics.png`

---

### Evidence ID: E04
- **Date:** 2026-09-05
- **Time:** 15:30 UTC
- **Oracle Service:** Oracle Autonomous JSON Database (SODA REST)
- **Action Performed:** Initialized SODA collection `feedback_collection` and inserted JSON document payloads via HTTPS REST POST.
- **Result:** JSON documents persisted in Autonomous DB without SQL schema setup.
- **Screenshot Filename:** `evidence/DATABASE/04-soda-json-documents.png`

---

### Evidence ID: E05
- **Date:** 2026-09-05
- **Time:** 16:00 UTC
- **Oracle Service:** React Telemetry Client
- **Action Performed:** Interacted with feedback submission UI and rendered sentiment distribution charts.
- **Result:** Verified end-to-end data pipeline from API Gateway down to SODA JSON storage.
- **Screenshot Filename:** `evidence/OCI/05-react-dashboard-live.png`
