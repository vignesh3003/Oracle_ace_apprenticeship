import logging
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from app.services.embeddings import generate_vector_embedding
from app.db.vector_store import search_similar_chunks
from app.config import settings

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/search", tags=["Vector Search"])

class SearchResultItem(BaseModel):
    chunk_id: str
    document_name: str
    chunk_index: int
    chunk_text: str
    distance: float
    similarity_score_pct: float

class SearchResponse(BaseModel):
    query: str
    top_k: int
    execution_engine: str
    results: List[SearchResultItem]

@router.get("", response_model=SearchResponse)
async def semantic_vector_search(
    q: str = Query(..., min_length=2, description="Natural language search query"),
    top_k: int = Query(5, ge=1, le=20, description="Number of top matches to return")
):
    """
    Perform natural language semantic vector search using Oracle Database 23ai native VECTOR_DISTANCE(..., COSINE).
    """
    try:
        # 1. Generate query embedding vector (384-dim)
        query_vector = generate_vector_embedding(q)

        # 2. Query Oracle Database 23ai VECTOR column using COSINE distance
        results = search_similar_chunks(query_vector=query_vector, top_k=top_k)

        engine = "Oracle Database 23ai (Native VECTOR_DISTANCE)" if not settings.is_demo_mode else "Oracle 23ai Simulation Engine (Cosine Distance)"

        return SearchResponse(
            query=q,
            top_k=top_k,
            execution_engine=engine,
            results=results
        )
    except Exception as e:
        logger.error(f"[Search API Error] {e}")
        raise HTTPException(status_code=500, detail=f"Error executing vector search: {str(e)}")
