-- OracleGenAI-RAG Chat History Table DDL
CREATE TABLE IF NOT EXISTS genai_chat_history (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    prompt CLOB NOT NULL,
    response CLOB NOT NULL,
    model_id VARCHAR2(100) DEFAULT 'cohere.command-r-plus',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

COMMIT;
