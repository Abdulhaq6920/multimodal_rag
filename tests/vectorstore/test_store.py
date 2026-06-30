from app.config import UPLOAD_DIR
from app.ingestion.chunker import chunk_documents
from app.ingestion.document_builder import build_documents
from app.ingestion.parser import parse_pdf
from app.ingestion.processor import process_elements
from app.vectorstore.store import add_documents


pdf_path = UPLOAD_DIR / "attention-is-all-you-need-Paper.pdf"

elements = parse_pdf(pdf_path)

processed = process_elements(elements)

# ---------------------------------------
# Dummy captions
# ---------------------------------------

images = []

for index, image in enumerate(processed["images"], start=1):

    images.append(
        {
            "caption": f"Dummy caption {index}",
            "page": image.metadata.page_number,
            "image_path": f"uploads/images/image_{index}.jpg",
        }
    )

documents = build_documents(
    texts=processed["texts"],
    tables=processed["tables"],
    images=images,
    source_name=pdf_path.name,
)

chunked_documents = chunk_documents(documents)

add_documents(chunked_documents)