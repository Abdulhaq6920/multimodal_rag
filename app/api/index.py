from fastapi import APIRouter

from app.api.models import IndexResponse
from app.config import UPLOAD_DIR
from app.ingestion.pipeline import ingest_pdf

router = APIRouter(
    prefix="/index",
    tags=["Index"],
)


@router.post(
    "/",
    response_model=IndexResponse,
)
async def index_documents():
    """
    Index every uploaded PDF into Qdrant.
    """

    pdf_files = sorted(
        UPLOAD_DIR.glob("*.pdf")
    )

    if not pdf_files:
        return IndexResponse(
            indexed=[],
            failed=[],
            total_indexed=0,
        )

    indexed = []
    failed = []

    for pdf in pdf_files:

        try:

            print("=" * 60)
            print(f"Indexing : {pdf.name}")
            print("=" * 60)

            ingest_pdf(str(pdf))

            indexed.append(pdf.name)

        except Exception as e:

            failed.append(
                {
                    "file": pdf.name,
                    "error": str(e),
                }
            )

    return IndexResponse(
        indexed=indexed,
        failed=failed,
        total_indexed=len(indexed),
    )