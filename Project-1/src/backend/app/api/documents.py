import logging
from typing import List, Dict, Any
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from pydantic import BaseModel
from app.services.oci_vision import process_document_with_oci_vision
from app.services.embeddings import chunk_text_and_embed
from app.db.vector_store import insert_document_and_chunks, get_all_documents
from app.config import settings

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/documents", tags=["Documents & Ingestion"])

class DocumentResponse(BaseModel):
    id: int
    document_name: str
    storage_object_name: str
    file_type: str
    file_size_bytes: int
    ocr_status: str
    confidence_score: float
    created_at: str

class UploadResponse(BaseModel):
    message: str
    document_id: int
    document_name: str
    confidence_score: float
    total_chunks: int
    oracle_services_invoked: List[str]

@router.post("/upload", response_model=UploadResponse, status_code=status.HTTP_201_CREATED)
async def upload_and_process_document(file: UploadFile = File(...)):
    """
    Upload document (PDF / Image), run OCI Vision OCR, generate vector embeddings, 
    and store native VECTOR data into Oracle Database 23ai.
    """
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename missing.")

    contents = await file.read()
    file_size = len(contents)

    if file_size == 0:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    try:
        # 1. OCI Vision OCR Processing
        extracted_text, confidence, lines = process_document_with_oci_vision(contents, file.filename)

        # 2. Chunking & 384-dim Vector Embedding Generation
        chunks = chunk_text_and_embed(extracted_text, chunk_size_words=80)

        # 3. Store into Oracle Autonomous Database 23ai
        storage_object_name = f"doc_{file.filename}"
        doc_id = insert_document_and_chunks(
            document_name=file.filename,
            storage_object_name=storage_object_name,
            file_type=file.content_type or "application/octet-stream",
            file_size_bytes=file_size,
            confidence_score=confidence,
            chunks=chunks
        )

        services_used = ["Oracle Autonomous Database 23ai (AI Vector Search)"]
        if not settings.is_demo_mode:
            services_used.extend(["OCI Vision AI Service", "OCI Object Storage"])
        else:
            services_used.append("OCI SDK Client (Demo Simulation Mode)")

        return UploadResponse(
            message="Document successfully processed and indexed in Oracle Database 23ai.",
            document_id=doc_id,
            document_name=file.filename,
            confidence_score=confidence,
            total_chunks=len(chunks),
            oracle_services_invoked=services_used
        )
    except Exception as e:
        logger.error(f"[Upload Route Error] Failed to process document: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error processing document: {str(e)}")

@router.get("", response_model=List[DocumentResponse])
async def list_documents():
    """Retrieve list of indexed documents from Oracle Autonomous Database 23ai."""
    try:
        docs = get_all_documents()
        return docs
    except Exception as e:
        logger.error(f"[List Documents Error] {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch documents from Oracle Database.")
