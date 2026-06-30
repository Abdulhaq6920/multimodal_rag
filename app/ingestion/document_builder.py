from langchain_core.documents import Document


def build_documents(
    texts,
    tables,
    images,
    source_name: str,
):
    """
    Convert parsed PDF elements into LangChain Documents.

    Args:
        texts: List of text elements.
        tables: List of table elements.
        images: List of dictionaries containing:
                {
                    "caption": str,
                    "page": int,
                    "image_path": str
                }
        source_name: PDF filename.

    Returns:
        List[Document]
    """

    documents = []

    # -----------------------------
    # Text Documents
    # -----------------------------

    for text in texts:

        documents.append(
            Document(
                page_content=str(text),
                metadata={
                    "type": "text",
                    "page": text.metadata.page_number,
                    "source": source_name,
                },
            )
        )

    # -----------------------------
    # Table Documents
    # -----------------------------

    for table in tables:

        html = getattr(
            table.metadata,
            "text_as_html",
            None,
        )

        documents.append(
            Document(
                page_content=html if html else str(table),
                metadata={
                    "type": "table",
                    "page": table.metadata.page_number,
                    "source": source_name,
                },
            )
        )

    # -----------------------------
    # Image Documents
    # -----------------------------

    for image in images:

        documents.append(
            Document(
                page_content=image["caption"],
                metadata={
                    "type": "image",
                    "page": image["page"],
                    "source": source_name,
                    "image_path": image["image_path"],
                },
            )
        )

    return documents