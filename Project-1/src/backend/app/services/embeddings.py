import logging
import uuid
import numpy as np
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

_model = None

def get_embedding_model():
    """Lazy load sentence-transformers model (all-MiniLM-L6-v2 produces 384-dim vectors matching Oracle 23ai DDL)."""
    global _model
    if _model is None:
        try:
            from sentence_transformers import SentenceTransformer
            _model = SentenceTransformer('all-MiniLM-L6-v2')
            logger.info("[Embeddings] Loaded SentenceTransformer model 'all-MiniLM-L6-v2' (384-dim).")
        except Exception as e:
            logger.warning(f"[Embeddings] SentenceTransformers model load failed/skipped: {e}. Using lightweight vector generator.")
            _model = "lightweight"
    return _model

def generate_vector_embedding(text: str) -> List[float]:
    """Generate a 384-dimensional vector embedding for text input."""
    model = get_embedding_model()
    if model != "lightweight" and hasattr(model, 'encode'):
        try:
            embedding = model.encode(text, convert_to_numpy=True)
            return embedding.astype(float).tolist()
        except Exception as e:
            logger.error(f"[Embeddings] Model encoding failed: {e}")

    # Deterministic 384-dim normalized pseudo-embedding fallback
    np.random.seed(abs(hash(text)) % (2**32))
    vec = np.random.uniform(-1.0, 1.0, size=384)
    norm = np.linalg.norm(vec)
    if norm > 0:
        vec = vec / norm
    return vec.astype(float).tolist()

def chunk_text_and_embed(text: str, chunk_size_words: int = 100) -> List[Dict[str, Any]]:
    """Split text into chunks and generate 384-dim vector embeddings for each chunk."""
    words = text.split()
    if not words:
        words = ["Empty", "document"]

    chunks = []
    chunk_index = 0
    for i in range(0, len(words), chunk_size_words):
        chunk_words = words[i:i + chunk_size_words]
        chunk_text = " ".join(chunk_words)
        embedding = generate_vector_embedding(chunk_text)

        chunks.append({
            "chunk_id": f"chk_{uuid.uuid4().hex[:12]}",
            "chunk_index": chunk_index,
            "chunk_text": chunk_text,
            "token_count": len(chunk_words),
            "embedding": embedding
        })
        chunk_index += 1

    return chunks
