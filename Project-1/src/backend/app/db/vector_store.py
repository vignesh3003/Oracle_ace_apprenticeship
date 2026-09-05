import logging
import numpy as np
from typing import List, Dict, Any
from app.config import settings
from app.db.connection import get_db_connection, _demo_documents_db, _demo_chunks_db, _demo_id_counter

logger = logging.getLogger(__name__)

def insert_document_and_chunks(
    document_name: str,
    storage_object_name: str,
    file_type: str,
    file_size_bytes: int,
    confidence_score: float,
    chunks: List[Dict[str, Any]]
) -> int:
    """Insert document metadata and vector embeddings into Oracle 23ai or demo store."""
    global _demo_id_counter
    conn = get_db_connection()

    if conn is not None:
        try:
            cursor = conn.cursor()
            # 1. Insert Master Document Record
            doc_id_var = cursor.var(int)
            insert_doc_sql = """
                INSERT INTO documents (document_name, storage_object_name, file_type, file_size_bytes, ocr_status, confidence_score)
                VALUES (:1, :2, :3, :4, 'COMPLETED', :5)
                RETURNING id INTO :6
            """
            cursor.execute(insert_doc_sql, (document_name, storage_object_name, file_type, file_size_bytes, confidence_score, doc_id_var))
            doc_id = doc_id_var.getvalue()[0]

            # 2. Insert Vector Embedding Chunks into Oracle 23ai
            insert_chunk_sql = """
                INSERT INTO document_chunks (chunk_id, document_id, chunk_index, chunk_text, token_count, embedding)
                VALUES (:1, :2, :3, :4, :5, :6)
            """
            for chunk in chunks:
                # Convert float vector list to Oracle array or array format
                cursor.execute(insert_chunk_sql, (
                    chunk["chunk_id"],
                    doc_id,
                    chunk["chunk_index"],
                    chunk["chunk_text"],
                    chunk["token_count"],
                    chunk["embedding"] # python-oracledb supports Python list of floats for 23ai VECTOR
                ))

            conn.commit()
            cursor.close()
            conn.close()
            logger.info(f"[Oracle DB 23ai] Stored document ID {doc_id} with {len(chunks)} vector chunks.")
            return doc_id
        except Exception as e:
            logger.error(f"[Oracle DB 23ai] Error inserting document/chunks: {e}")
            if conn:
                conn.rollback()
                conn.close()

    # Demo Simulation Fallback
    doc_id = _demo_id_counter
    _demo_id_counter += 1
    doc_record = {
        "id": doc_id,
        "document_name": document_name,
        "storage_object_name": storage_object_name,
        "file_type": file_type,
        "file_size_bytes": file_size_bytes,
        "ocr_status": "COMPLETED",
        "confidence_score": confidence_score,
        "created_at": "2026-09-05 12:00:00"
    }
    _demo_documents_db.append(doc_record)

    for chunk in chunks:
        _demo_chunks_db.append({
            "chunk_id": chunk["chunk_id"],
            "document_id": doc_id,
            "document_name": document_name,
            "chunk_index": chunk["chunk_index"],
            "chunk_text": chunk["chunk_text"],
            "token_count": chunk["token_count"],
            "embedding": chunk["embedding"]
        })

    logger.info(f"[Demo Storage] Stored document ID {doc_id} with {len(chunks)} vector chunks in-memory.")
    return doc_id

def search_similar_chunks(query_vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
    """Query vector embeddings using Oracle 23ai native VECTOR_DISTANCE(..., COSINE) or demo distance."""
    conn = get_db_connection()

    if conn is not None:
        try:
            cursor = conn.cursor()
            # Execute native Oracle Database 23ai VECTOR_DISTANCE query
            sql = """
                SELECT 
                    c.chunk_id,
                    d.document_name,
                    c.chunk_index,
                    c.chunk_text,
                    VECTOR_DISTANCE(c.embedding, :1, COSINE) AS distance
                FROM document_chunks c
                JOIN documents d ON c.document_id = d.id
                ORDER BY VECTOR_DISTANCE(c.embedding, :1, COSINE) ASC
                FETCH FIRST :2 ROWS ONLY
            """
            cursor.execute(sql, (query_vector, top_k))
            rows = cursor.fetchall()
            results = []
            for row in rows:
                dist = float(row[4])
                sim_pct = round(max(0.0, (1.0 - dist)) * 100, 2)
                results.append({
                    "chunk_id": row[0],
                    "document_name": row[1],
                    "chunk_index": row[2],
                    "chunk_text": row[3],
                    "distance": dist,
                    "similarity_score_pct": sim_pct
                })
            cursor.close()
            conn.close()
            return results
        except Exception as e:
            logger.error(f"[Oracle DB 23ai] Vector search query failed: {e}")
            if conn:
                conn.close()

    # Demo Simulation Fallback (Cosine similarity via numpy)
    if not _demo_chunks_db:
        return []

    q_arr = np.array(query_vector, dtype=np.float32)
    norm_q = np.linalg.norm(q_arr)
    if norm_q == 0:
        norm_q = 1.0

    scored_chunks = []
    for c in _demo_chunks_db:
        c_arr = np.array(c["embedding"], dtype=np.float32)
        norm_c = np.linalg.norm(c_arr)
        if norm_c == 0:
            norm_c = 1.0
        # Cosine distance = 1 - dot_product / (norm_a * norm_b)
        cosine_sim = float(np.dot(q_arr, c_arr) / (norm_q * norm_c))
        cosine_dist = float(1.0 - cosine_sim)
        sim_pct = round(max(0.0, cosine_sim) * 100, 2)

        scored_chunks.append({
            "chunk_id": c["chunk_id"],
            "document_name": c.get("document_name", "Document"),
            "chunk_index": c["chunk_index"],
            "chunk_text": c["chunk_text"],
            "distance": round(cosine_dist, 4),
            "similarity_score_pct": sim_pct
        })

    scored_chunks.sort(key=lambda x: x["distance"])
    return scored_chunks[:top_k]

def get_all_documents() -> List[Dict[str, Any]]:
    """Retrieve master document list from Oracle 23ai or demo store."""
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, document_name, storage_object_name, file_type, file_size_bytes, ocr_status, confidence_score, created_at FROM documents ORDER BY id DESC")
            rows = cursor.fetchall()
            results = []
            for r in rows:
                results.append({
                    "id": r[0],
                    "document_name": r[1],
                    "storage_object_name": r[2],
                    "file_type": r[3],
                    "file_size_bytes": r[4],
                    "ocr_status": r[5],
                    "confidence_score": float(r[6]) if r[6] else 95.0,
                    "created_at": str(r[7])
                })
            cursor.close()
            conn.close()
            return results
        except Exception as e:
            logger.error(f"[Oracle DB 23ai] Failed to fetch documents: {e}")
            if conn:
                conn.close()

    return _demo_documents_db
