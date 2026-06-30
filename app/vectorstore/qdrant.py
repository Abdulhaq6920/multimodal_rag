from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from app.config import settings


client = QdrantClient(
    url=settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY,
)


def create_collection(vector_size: int):
    """
    Create the Qdrant collection if it doesn't already exist.
    """

    collections = client.get_collections()

    existing = [
        collection.name
        for collection in collections.collections
    ]

    if settings.QDRANT_COLLECTION in existing:
        print("Collection already exists.")
        return

    client.create_collection(
        collection_name=settings.QDRANT_COLLECTION,
        vectors_config=VectorParams(
            size=vector_size,
            distance=Distance.COSINE,
        ),
    )

    print("Collection created successfully.")