from app.config import UPLOAD_DIR
from app.ingestion.pipeline import ingest_pdf

pdf = UPLOAD_DIR / "attention-is-all-you-need-Paper.pdf"

documents = ingest_pdf(pdf)

print()
print("=" * 60)
print("Pipeline Completed")
print("=" * 60)
print(f"Total Chunks : {len(documents)}")