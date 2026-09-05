#!/usr/bin/env python3
"""
Diagnostic Script: Test Oracle Autonomous Database 23ai Vector Search Connection
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))

from app.config import settings
from app.services.embeddings import generate_vector_embedding
from app.db.vector_store import search_similar_chunks, insert_document_and_chunks

def main():
    print("=" * 60)
    print("Oracle Autonomous Database 23ai Vector Search Diagnostic Test")
    print("=" * 60)
    print(f"Database DSN: {settings.ORACLE_DB_DSN}")
    print(f"Thin Mode: {settings.ORACLE_DB_THIN_MODE}")
    print("-" * 60)

    # Generate sample embedding
    sample_vec = generate_vector_embedding("Oracle 23ai AI Vector Search integration test")
    print(f"Generated Vector Dimensions: {len(sample_vec)} (Float32)")

    # Insert sample chunk
    chunks = [{
        "chunk_id": "test_chk_001",
        "chunk_index": 0,
        "chunk_text": "Oracle Database 23ai integrates AI Vector Search for RAG and semantic retrieval.",
        "token_count": 12,
        "embedding": sample_vec
    }]

    doc_id = insert_document_and_chunks(
        document_name="Test_23ai_Doc.pdf",
        storage_object_name="test_23ai_doc.pdf",
        file_type="application/pdf",
        file_size_bytes=2048,
        confidence_score=99.0,
        chunks=chunks
    )
    print(f"Inserted Document ID: {doc_id}")

    # Query vector distance
    results = search_similar_chunks(sample_vec, top_k=1)
    print(f"Top Match Result Count: {len(results)}")
    if results:
        top = results[0]
        print(f"Matched Text: {top['chunk_text']}")
        print(f"Cosine Distance: {top['distance']}")
        print(f"Similarity Score: {top['similarity_score_pct']}%")

    print("=" * 60)
    print("Oracle Database 23ai Test Execution Successful!")

if __name__ == "__main__":
    main()
