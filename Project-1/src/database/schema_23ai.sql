-- =============================================================================
-- OracleDocuAI: Oracle Autonomous Database 23ai DDL Schema
-- Demonstrating Native Oracle 23ai AI Vector Search Capabilities
-- =============================================================================

-- 1. Create Sequence for Document Tracking
CREATE SEQUENCE IF NOT EXISTS doc_seq START WITH 1 INCREMENT BY 1;

-- 2. Create Documents Master Table
CREATE TABLE IF NOT EXISTS documents (
    id NUMBER DEFAULT doc_seq.NEXTVAL PRIMARY KEY,
    document_name VARCHAR2(255) NOT NULL,
    storage_object_name VARCHAR2(500) NOT NULL,
    file_type VARCHAR2(50) NOT NULL,
    file_size_bytes NUMBER,
    ocr_status VARCHAR2(50) DEFAULT 'PENDING',
    confidence_score NUMBER(5, 2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Create Document Vector Chunks Table (Oracle Database 23ai VECTOR Column)
-- Note: VECTOR(384, FLOAT32) specifies 384 dimensions using standard 32-bit floating point.
CREATE TABLE IF NOT EXISTS document_chunks (
    chunk_id VARCHAR2(100) PRIMARY KEY,
    document_id NUMBER REFERENCES documents(id) ON DELETE CASCADE,
    chunk_index NUMBER NOT NULL,
    chunk_text CLOB NOT NULL,
    token_count NUMBER,
    embedding VECTOR(384, FLOAT32),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 4. Create Inverted In-Memory Vector Index for Fast Cosine Similarity
-- Oracle 23ai Vector Index creation syntax:
CREATE VECTOR INDEX IF NOT EXISTS doc_chunks_vec_idx 
ON document_chunks (embedding)
ORGANIZATION INMEMORY NEIGHBOR GRAPH
DISTANCE COSINE
WITH TARGET ACCURACY 95;

-- 5. Create System Processing Log Table
CREATE TABLE IF NOT EXISTS system_logs (
    log_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    operation VARCHAR2(100) NOT NULL,
    status VARCHAR2(50) NOT NULL,
    details CLOB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

COMMIT;
