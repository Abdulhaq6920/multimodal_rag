from app.config import UPLOAD_DIR
from app.ingestion.parser import parse_pdf


pdf_file = UPLOAD_DIR / "attention-is-all-you-need-Paper.pdf"

elements = parse_pdf(pdf_file)

print("=" * 60)
print(f"Total Elements : {len(elements)}")
print("=" * 60)

for index, element in enumerate(elements, start=1):
    print(f"{index}. {element.category}")