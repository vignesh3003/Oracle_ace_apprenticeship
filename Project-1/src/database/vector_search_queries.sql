-- =============================================================================
-- OracleDocuAI: Sample Vector Search Queries for Oracle Database 23ai
-- Demonstrates COSINE, EUCLIDEAN, and DOT product distance metrics
-- =============================================================================

-- Query 1: Top 5 most semantically similar document chunks using COSINE distance
SELECT 
    c.chunk_id,
    d.document_name,
    c.chunk_index,
    c.chunk_text,
    ROUND(VECTOR_DISTANCE(c.embedding, :query_vector, COSINE), 4) AS distance,
    ROUND((1 - VECTOR_DISTANCE(c.embedding, :query_vector, COSINE)) * 100, 2) AS similarity_score_pct
FROM document_chunks c
JOIN documents d ON c.document_id = d.id
ORDER BY VECTOR_DISTANCE(c.embedding, :query_vector, COSINE) ASC
FETCH FIRST 5 ROWS ONLY;

-- Query 2: Filter by document ID and perform semantic search within single document
SELECT 
    c.chunk_id,
    c.chunk_index,
    c.chunk_text,
    VECTOR_DISTANCE(c.embedding, :query_vector, COSINE) AS distance
FROM document_chunks c
WHERE c.document_id = :target_doc_id
ORDER BY distance ASC;

-- Query 3: Aggregate vector metrics per document
SELECT 
    d.id,
    d.document_name,
    COUNT(c.chunk_id) AS total_chunks,
    MAX(c.created_at) AS last_indexed_time
FROM documents d
LEFT JOIN document_chunks c ON d.id = c.document_id
GROUP BY d.id, d.document_name;
