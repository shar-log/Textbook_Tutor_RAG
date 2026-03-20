from fastapi import APIRouter, UploadFile, File
import shutil
import os

from backend.config import UPLOAD_DIR
from backend.ingestion.pipeline import run_pipeline

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    print("[UPLOAD] Received file:", file.filename)

    save_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save file
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print("[UPLOAD] Saved to:", save_path)

    # Run ingestion pipeline
    chunks = run_pipeline(save_path)

    print("[UPLOAD] Pipeline finished")

    return {
        "filename": file.filename,
        "chunks_created": len(chunks)
    }