import logging
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.core.oci_speech import process_audio_transcription
from app.db.connection import save_media_transcript, get_transcripts

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/transcribe", tags=["OCI Speech AI"])

@router.post("/upload")
async def upload_and_transcribe(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename missing.")
    contents = await file.read()
    if len(contents) == 0:
        raise HTTPException(status_code=400, detail="File is empty.")

    try:
        transcript, conf, job_ocid = process_audio_transcription(file.filename, contents)
        record_id = save_media_transcript(file.filename, transcript, conf)
        return {
            "record_id": record_id,
            "filename": file.filename,
            "transcript": transcript,
            "confidence_score": conf,
            "job_ocid": job_ocid,
            "oracle_services": ["OCI Speech AI Service", "OCI Object Storage", "Oracle Autonomous DB"]
        }
    except Exception as e:
        logger.error(f"[Transcribe API Error] {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/list")
def list_history():
    return get_transcripts()
