import logging
from typing import List, Dict, Any
from app.config import settings

logger = logging.getLogger(__name__)

_demo_conversations_db: List[Dict[str, Any]] = [
    {
        "id": 1,
        "prompt": "What are the security features of OCI Generative AI Service?",
        "response": "OCI Generative AI provides dedicated AI clusters and isolated tenancy inference. Prompts are never retained or used to train base foundation models.",
        "model_id": "cohere.command-r-plus",
        "created_at": "2026-09-16 10:00:00"
    }
]
_conv_id_seq = 2

def save_chat_conversation(prompt: str, response: str, model_id: str) -> int:
    global _conv_id_seq
    if not settings.is_demo_mode:
        try:
            import oracledb
            conn = oracledb.connect(
                user=settings.ORACLE_DB_USER,
                password=settings.ORACLE_DB_PASSWORD,
                dsn=settings.ORACLE_DB_DSN
            )
            cursor = conn.cursor()
            sql = "INSERT INTO genai_chat_history (prompt, response, model_id) VALUES (:1, :2, :3) RETURNING id INTO :4"
            out_var = cursor.var(int)
            cursor.execute(sql, (prompt, response, model_id, out_var))
            conn.commit()
            c_id = out_var.getvalue()[0]
            cursor.close()
            conn.close()
            return c_id
        except Exception as e:
            logger.error(f"[Oracle DB] Chat record save error: {e}")

    c_id = _conv_id_seq
    _conv_id_seq += 1
    _demo_conversations_db.insert(0, {
        "id": c_id,
        "prompt": prompt,
        "response": response,
        "model_id": model_id,
        "created_at": "2026-09-16 12:00:00"
    })
    return c_id

def get_chat_history() -> List[Dict[str, Any]]:
    if not settings.is_demo_mode:
        try:
            import oracledb
            conn = oracledb.connect(
                user=settings.ORACLE_DB_USER,
                password=settings.ORACLE_DB_PASSWORD,
                dsn=settings.ORACLE_DB_DSN
            )
            cursor = conn.cursor()
            cursor.execute("SELECT id, prompt, response, model_id, created_at FROM genai_chat_history ORDER BY id DESC FETCH FIRST 10 ROWS ONLY")
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            return [{"id": r[0], "prompt": r[1], "response": r[2], "model_id": r[3], "created_at": str(r[4])} for r in rows]
        except Exception as e:
            logger.error(f"[Oracle DB] Chat history query error: {e}")

    return _demo_conversations_db
