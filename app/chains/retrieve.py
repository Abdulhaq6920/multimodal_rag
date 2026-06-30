from app.retriever.retriever import get_retriever
from app.retriever.formatter import format_context

retriever = get_retriever()


def build_sources(documents):
    """
    Convert retrieved documents into source metadata
    for the frontend.
    """

    sources = []
    seen = set()

    for doc in documents:

        source = {
            "document": doc.metadata.get("source", "Unknown"),
            "page": doc.metadata.get("page", "-"),
            "type": doc.metadata.get("type", "text"),
        }

        key = (
            source["document"],
            source["page"],
            source["type"],
        )

        if key not in seen:
            seen.add(key)
            sources.append(source)

    return sources


def retrieve_documents(question: str):
    """
    Retrieve documents from Qdrant and prepare
    context + sources.
    """

    documents = retriever.invoke(question)

    context = format_context(documents)

    sources = build_sources(documents)

    return {
        "documents": documents,
        "context": context,
        "sources": sources,
    }