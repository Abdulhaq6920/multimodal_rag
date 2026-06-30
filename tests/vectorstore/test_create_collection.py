from app.embeddings.text_embedding import embedding_model
from app.vectorstore.qdrant import create_collection

sample_vector = embedding_model.embed_query(
    "Hello World"
)

vector_size = len(sample_vector)

print(f"Vector Dimension : {vector_size}")

create_collection(vector_size)