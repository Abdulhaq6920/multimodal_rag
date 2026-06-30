from pathlib import Path

from app.config import IMAGE_DIR
from app.ingestion.chunker import chunk_documents
from app.ingestion.document_builder import build_documents
from app.ingestion.parser import parse_pdf
from app.ingestion.processor import process_elements
from app.vectorstore.store import add_documents
from app.vision.caption import generate_caption


def ingest_pdf(pdf_path: str):
    """
    Complete ingestion pipeline.

    PDF
        ↓
    Parse
        ↓
    Process
        ↓
    Caption Images
        ↓
    Build Documents
        ↓
    Chunk
        ↓
    Store in Qdrant
    """

    pdf_path = Path(pdf_path)

    print("=" * 60)
    print(f"Ingesting : {pdf_path.name}")
    print("=" * 60)

    # --------------------------------------------------
    # Create image directory for this PDF
    # --------------------------------------------------

    image_dir = IMAGE_DIR / pdf_path.stem

    image_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    # --------------------------------------------------
    # Parse PDF
    # --------------------------------------------------

    elements = parse_pdf(
        pdf_path=pdf_path,
        image_output_dir=image_dir,
    )

    # --------------------------------------------------
    # Separate elements
    # --------------------------------------------------

    processed = process_elements(elements)

    # --------------------------------------------------
    # Generate captions for extracted images
    # --------------------------------------------------

    images = []

    image_files = sorted(image_dir.glob("*"))

    for element, image_path in zip(
        processed["images"],
        image_files,
    ):

        caption = generate_caption(image_path)

        images.append(
            {
                "caption": caption,
                "page": element.metadata.page_number,
                "image_path": str(image_path),
            }
        )

    # --------------------------------------------------
    # Build LangChain Documents
    # --------------------------------------------------

    documents = build_documents(
        texts=processed["texts"],
        tables=processed["tables"],
        images=images,
        source_name=pdf_path.name,
    )

    # --------------------------------------------------
    # Chunk Documents
    # --------------------------------------------------

    chunked_documents = chunk_documents(
        documents
    )

    # --------------------------------------------------
    # Store in Qdrant
    # --------------------------------------------------

    add_documents(chunked_documents)

    print()
    print("✅ Ingestion completed successfully.")
    print(
        f"Documents Stored : {len(chunked_documents)}"
    )

    return chunked_documents