from pathlib import Path

from unstructured.partition.pdf import partition_pdf

from app.config import PDF_PARSE_STRATEGY


def parse_pdf(
    pdf_path: str,
    image_output_dir: str,
):
    """
    Parse a PDF using Unstructured.

    Images extracted from the PDF are saved
    into the provided image_output_dir.
    """

    pdf_path = Path(pdf_path)

    image_output_dir = Path(image_output_dir)
    image_output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    if not pdf_path.exists():
        raise FileNotFoundError(
            f"{pdf_path} does not exist."
        )

    elements = partition_pdf(
        filename=str(pdf_path),
        strategy=PDF_PARSE_STRATEGY,
        infer_table_structure=True,
        extract_image_block_types=["Image"],
        extract_image_block_output_dir=str(image_output_dir),
    )

    return elements