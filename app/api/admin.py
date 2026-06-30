import shutil

from fastapi import (
    APIRouter,
    HTTPException,
)

from app.api.models import MessageResponse
from app.config import (
    IMAGE_DIR,
    UPLOAD_DIR,
)
from app.embeddings.text_embedding import embedding_model
from app.memory.history import clear_chat_history
from app.vectorstore.delete import (
    delete_all_vectors,
    delete_document_vectors,
)
from app.vectorstore.qdrant import (
    create_collection,
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.delete(
    "/pdf/{filename}",
    response_model=MessageResponse,
)
async def delete_pdf(filename: str):
    """
    Delete a single uploaded PDF together with:
    - extracted images
    - vectors stored in Qdrant
    """

    pdf_path = UPLOAD_DIR / filename

    if not pdf_path.exists():
        raise HTTPException(
            status_code=404,
            detail="PDF not found.",
        )

    # ----------------------------------------
    # Delete uploaded PDF
    # ----------------------------------------

    pdf_path.unlink()

    # ----------------------------------------
    # Delete extracted images
    # ----------------------------------------

    image_folder = IMAGE_DIR / pdf_path.stem

    if image_folder.exists():
        shutil.rmtree(image_folder)

    # ----------------------------------------
    # Delete vectors
    # ----------------------------------------

    delete_document_vectors(filename)

    return MessageResponse(
        message=f"{filename} deleted successfully."
    )


@router.post(
    "/reset",
    response_model=MessageResponse,
)
async def reset_chatbot():
    """
    Reset the complete chatbot.

    Removes:
    - uploaded PDFs
    - extracted images
    - chat history
    - vector database
    """

    # ----------------------------------------
    # Clear memory
    # ----------------------------------------

    clear_chat_history()

    # ----------------------------------------
    # Delete uploaded PDFs
    # ----------------------------------------

    if UPLOAD_DIR.exists():

        for pdf in UPLOAD_DIR.glob("*"):

            if pdf.is_file():
                pdf.unlink()

    # ----------------------------------------
    # Delete extracted images
    # ----------------------------------------

    if IMAGE_DIR.exists():
        shutil.rmtree(IMAGE_DIR)

    IMAGE_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    # ----------------------------------------
    # Reset Qdrant
    # ----------------------------------------

    delete_all_vectors()

    vector_size = len(
        embedding_model.embed_query("hello")
    )

    create_collection(vector_size)

    return MessageResponse(
        message="Chatbot reset successfully."
    )