from app.config import (
    settings,
    CHUNK_SIZE,
    MEMORY_WINDOW,
    PDF_PARSE_STRATEGY,
)

print("=" * 50)
print("Configuration Test")
print("=" * 50)

print(f"GROQ Model        : {settings.GROQ_MODEL}")
print(f"Qdrant Collection : {settings.QDRANT_COLLECTION}")
print(f"Chunk Size        : {CHUNK_SIZE}")
print(f"Memory Window     : {MEMORY_WINDOW}")
print(f"Parser Strategy   : {PDF_PARSE_STRATEGY}")

print("\nConfiguration loaded successfully.")