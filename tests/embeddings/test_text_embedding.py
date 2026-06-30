from app.embeddings.text_embedding import embedding_model

text = """
Retrieval Augmented Generation combines
vector search with Large Language Models.
"""

vector = embedding_model.embed_query(text)

print("=" * 60)
print("Embedding Test")
print("=" * 60)

print(f"Vector Dimension : {len(vector)}")

print(f"\nFirst 10 Values:\n")

print(vector[:10])