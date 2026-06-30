from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
)


def chunk_documents(documents):
    """
    Split LangChain Documents into smaller chunks.

    Args:
        documents: List[Document]

    Returns:
        List[Document]
    """

    chunked_documents = text_splitter.split_documents(
        documents
    )

    return chunked_documents