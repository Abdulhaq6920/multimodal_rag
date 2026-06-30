from app.chains.rag import get_rag_chain


chain = get_rag_chain()

response = chain.invoke(
    {
        "question": "What is self attention?",
        "history": [],
    }
)

print("=" * 60)
print(response)
print("=" * 60)