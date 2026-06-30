from app.retriever.retriever import retriever

query = "What is self attention?"

documents = retriever.invoke(query)

print("=" * 60)

print(f"Retrieved : {len(documents)}")

print("=" * 60)

for doc in documents:

    print(doc.metadata)

    print(doc.page_content[:300])

    print("-" * 60)