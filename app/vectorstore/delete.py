from qdrant_client.models import (
    FieldCondition,
    Filter,
    FilterSelector,
    MatchValue,
)

from app.config import settings
from app.vectorstore.qdrant import client


def delete_document_vectors(filename: str):
    """
    Delete every vector belonging to a PDF.
    """

    client.delete(
        collection_name=settings.QDRANT_COLLECTION,
        points_selector=FilterSelector(
            filter=Filter(
                must=[
                    FieldCondition(
                        key="metadata.source",
                        match=MatchValue(
                            value=filename
                        ),
                    )
                ]
            )
        ),
    )


def delete_all_vectors():
    """
    Delete the complete collection.
    """

    client.delete_collection(
        collection_name=settings.QDRANT_COLLECTION
    )