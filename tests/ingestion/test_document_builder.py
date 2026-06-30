from pathlib import Path

from app.config import UPLOAD_DIR
from app.ingestion.document_builder import build_documents
from app.ingestion.parser import parse_pdf
from app.ingestion.processor import process_elements


pdf_path = UPLOAD_DIR / "attention-is-all-you-need-Paper.pdf"

elements = parse_pdf(pdf_path)

processed = process_elements(elements)


# ------------------------------------------------
# Dummy image caption for testing
# (Will be replaced by Groq Vision pipeline later)
# ------------------------------------------------

images = []

for index, image in enumerate(processed["images"], start=1):

    images.append(
        {
            "caption": f"Dummy caption for image {index}",
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


print("=" * 60)
print(f"Total Documents : {len(documents)}")
print("=" * 60)

print()

for document in documents[:10]:

    print(document.metadata)