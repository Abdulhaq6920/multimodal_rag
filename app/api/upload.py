from pathlib import Path

from fastapi import (
    APIRouter,
    File,
    HTTPException,
    UploadFile,
)

from app.api.models import (
    MessageResponse,
    UploadedFilesResponse,
)
from app.config import UPLOAD_DIR

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


@router.post(
    "/",
    response_model=MessageResponse,
)
async def upload_pdf(
    file: UploadFile = File(...),
):
    """
    Upload a single PDF.

    The file is only saved.
    No indexing is performed.
    """

    # -----------------------------
    # Validate filename
    # -----------------------------

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is missing.",
        )

    # -----------------------------
    # Validate extension
    # -----------------------------

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed.",
        )

    destination = Path(UPLOAD_DIR) / file.filename

    # -----------------------------
    # Prevent duplicate uploads
    # -----------------------------

    if destination.exists():
        raise HTTPException(
            status_code=409,
            detail=f"{file.filename} already exists.",
        )

    # -----------------------------
    # Save file
    # -----------------------------

    contents = await file.read()

    with open(destination, "wb") as pdf:
        pdf.write(contents)

    return MessageResponse(
        message=f"{file.filename} uploaded successfully."
    )


@router.get(
    "/files",
    response_model=UploadedFilesResponse,
)
async def list_uploaded_files():
    """
    Return all uploaded PDFs.
    """

    pdf_files = sorted(
        pdf.name
        for pdf in UPLOAD_DIR.glob("*.pdf")
    )

    return UploadedFilesResponse(
        total_files=len(pdf_files),
        files=pdf_files,
    )