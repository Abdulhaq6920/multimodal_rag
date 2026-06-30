from app.vectorstore.qdrant import client

collections = client.get_collections()

print("=" * 50)
print("Qdrant Connection Successful")
print("=" * 50)

for collection in collections.collections:
    print(collection.name)