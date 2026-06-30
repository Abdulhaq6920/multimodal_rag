from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.index import router as index_router
from app.api.chat import router as chat_router
from app.api.admin import router as admin_router


app = FastAPI(
    title="Multimodal RAG API",
    version="1.0.0",
    description="Backend API for Multimodal Retrieval-Augmented Generation",
)

# ---------------------------------------------------
# CORS
# ---------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------
# Routers
# ---------------------------------------------------

app.include_router(upload_router)
app.include_router(index_router)
app.include_router(chat_router)
app.include_router(admin_router)

# ---------------------------------------------------
# Health
# ---------------------------------------------------

@app.get("/")
async def root():
    return {
        "message": "Multimodal RAG Backend Running 🚀"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }