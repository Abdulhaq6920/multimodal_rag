from app.config import UPLOAD_DIR
from app.ingestion.parser import parse_pdf
from app.ingestion.processor import process_elements

pdf = UPLOAD_DIR / "attention-is-all-you-need-Paper.pdf"

elements = parse_pdf(pdf)

processed = process_elements(elements)

print("=" * 50)

print(f"Text Elements   : {len(processed['texts'])}")

print(f"Table Elements  : {len(processed['tables'])}")

print(f"Image Elements  : {len(processed['images'])}")

print("=" * 50)