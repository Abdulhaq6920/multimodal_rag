from langchain_qdrant import QdrantVectorStore

from app.config import settings
from app.embeddings.text_embedding import embedding_model
from app.vectorstore.qdrant import client


def get_vectorstore():
    """
    Return a LangChain QdrantVectorStore instance.
    """

    return QdrantVectorStore(
        client=client,
        collection_name=settings.QDRANT_COLLECTION,
        embedding=embedding_model,
    )


def add_documents(documents):
    """
    Add LangChain Documents to Qdrant.
    """

    vectorstore = get_vectorstore()

    vectorstore.add_documents(documents)

    print(f"Stored {len(documents)} documents in Qdrant.")