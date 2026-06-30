from pydantic import BaseModel


# ======================================================
# Chat
# ======================================================

class Source(BaseModel):
    document: str
    page: int | str
    type: str


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]


# ======================================================
# Common
# ======================================================

class MessageResponse(BaseModel):
    message: str


# ======================================================
# Upload
# ======================================================

class UploadedFilesResponse(BaseModel):
    total_files: int
    files: list[str]


# ======================================================
# Index
# ======================================================

class IndexResponse(BaseModel):
    indexed: list[str]
    failed: list[dict]
    total_indexed: int