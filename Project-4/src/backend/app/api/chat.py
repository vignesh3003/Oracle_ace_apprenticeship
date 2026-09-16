import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.oci_genai import generate_llm_response
from app.db.connection import save_chat_conversation, get_chat_history

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/genai", tags=["OCI Generative AI"])

class ChatRequest(BaseModel):
    prompt: str

@router.post("/chat")
def chat_with_genai(payload: ChatRequest):
    if not payload.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt text cannot be empty.")

    try:
        response_text, model_id, latency = generate_llm_response(payload.prompt)
        chat_id = save_chat_conversation(payload.prompt, response_text, model_id)
        return {
            "chat_id": chat_id,
            "prompt": payload.prompt,
            "response": response_text,
            "model_id": model_id,
            "latency_ms": latency,
            "oracle_services": ["OCI Generative AI Service", "Oracle Autonomous Database", "OCI Object Storage"]
        }
    except Exception as e:
        logger.error(f"[Chat API Error] {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history")
def fetch_history():
    return get_chat_history()
