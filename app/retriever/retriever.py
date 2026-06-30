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


def get_retriever():
    """
    Return a configured Qdrant retriever.
    """

    vectorstore = get_vectorstore()

    return vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 5,
        },
    )