import logging
from typing import List, Dict, Any
from app.config import settings

logger = logging.getLogger(__name__)

_demo_transcripts_db: List[Dict[str, Any]] = [
    {
        "id": 1,
        "media_name": "OCI_Architecture_Keynote.mp3",
        "transcript": "Oracle Speech AI Service delivers high-accuracy automatic speech recognition.",
        "confidence_score": 98.2,
        "created_at": "2026-09-16 14:00:00"
    }
]
_seq = 2

def save_media_transcript(name: str, text: str, conf: float) -> int:
    global _seq
    c_id = _seq
    _seq += 1
    _demo_transcripts_db.insert(0, {
        "id": c_id, "media_name": name, "transcript": text, "confidence_score": conf, "created_at": "2026-09-16 15:00:00"
    })
    return c_id

def get_transcripts() -> List[Dict[str, Any]]:
    return _demo_transcripts_db
