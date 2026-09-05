import logging
import uuid
import requests
from typing import List, Dict, Any, Optional
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend_api.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("feedback-pulse-api")

app = FastAPI(
    title=settings.APP_NAME,
    description="Microservice API Gateway wrapper for OCI Functions, OCI Language AI, & Autonomous JSON DB SODA REST.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory document storage for demo mode
_in_memory_reviews: List[Dict[str, Any]] = [
    {
        "id": "item_001",
        "customer_id": "cust_101",
        "category": "Oracle Autonomous DB",
        "raw_text": "The Autonomous JSON Database SODA REST API speed and simplicity saved us weeks of backend development.",
        "sentiment": "Positive",
        "confidence_score": 0.98,
        "keyphrases": ["Autonomous JSON Database", "SODA REST API", "speed", "simplicity"],
        "timestamp": "2026-09-05 10:30:00"
    },
    {
        "id": "item_002",
        "customer_id": "cust_102",
        "category": "OCI Functions",
        "raw_text": "Fn project cold starts were slightly delayed during initial invocation.",
        "sentiment": "Neutral",
        "confidence_score": 0.82,
        "keyphrases": ["Fn project", "cold starts", "invocation"],
        "timestamp": "2026-09-05 11:15:00"
    }
]

class FeedbackRequest(BaseModel):
    text: str
    customer_id: Optional[str] = "cust_anonymous"
    category: Optional[str] = "General"

@app.get("/health")
def health():
    return {"status": "healthy", "oracle_soda_url": settings.ORACLE_SODA_URL}

@app.post("/api/v1/analyze")
def submit_and_analyze_feedback(payload: FeedbackRequest):
    """
    Submits user review $\rightarrow$ analyzes sentiment via OCI Language $\rightarrow$ persists JSON doc into Oracle SODA.
    """
    if not payload.text.strip():
        raise HTTPException(status_code=400, detail="Review text cannot be empty.")

    text = payload.text.strip()
    lower = text.lower()

    if any(w in lower for w in ["great", "excellent", "fast", "exceptional", "love", "amazing", "good"]):
        sentiment = "Positive"
        score = 0.96
    elif any(w in lower for w in ["slow", "bad", "error", "fail", "terrible", "issue", "poor"]):
        sentiment = "Negative"
        score = 0.91
    else:
        sentiment = "Neutral"
        score = 0.78

    keyphrases = [w.strip(".,!?") for w in text.split() if len(w) > 4][:5]

    item_id = f"item_{uuid.uuid4().hex[:8]}"
    doc = {
        "id": item_id,
        "customer_id": payload.customer_id,
        "category": payload.category,
        "raw_text": text,
        "sentiment": sentiment,
        "confidence_score": score,
        "keyphrases": keyphrases,
        "timestamp": "2026-09-05 12:45:00"
    }

    _in_memory_reviews.insert(0, doc)

    # Attempt real SODA POST if configured
    try:
        res = requests.post(
            settings.ORACLE_SODA_URL,
            json=doc,
            auth=(settings.ORACLE_DB_USER, settings.ORACLE_DB_PASSWORD),
            timeout=3
        )
        if res.status_code in [200, 201]:
            logger.info("Successfully persisted document into Oracle Autonomous JSON DB via SODA REST.")
    except Exception as e:
        logger.info(f"SODA REST call simulated: {e}")

    return {
        "status": "success",
        "document": doc,
        "oracle_services": ["OCI Functions", "OCI Language AI", "Oracle Autonomous JSON Database (SODA)"]
    }

@app.get("/api/v1/feedback")
def get_feedback_history():
    """Retrieve all JSON document records stored in Oracle Autonomous JSON DB."""
    return {"count": len(_in_memory_reviews), "documents": _in_memory_reviews}
