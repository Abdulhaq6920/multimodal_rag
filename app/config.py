from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_DIR = BASE_DIR / "uploads"


class Settings(BaseSettings):

    GROQ_API_KEY: str
    GROQ_MODEL: str
    GROQ_VISION_MODEL: str

    QDRANT_URL: str
    QDRANT_API_KEY: str
    QDRANT_COLLECTION: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

settings = Settings()


PDF_PARSE_STRATEGY = "hi_res"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K = 5
MEMORY_WINDOW = 10
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

IMAGE_DIR = UPLOAD_DIR / "images"
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

# Future settings
# IMAGE_DESCRIPTION_MODEL = ...
# RERANKER_MODEL = ...