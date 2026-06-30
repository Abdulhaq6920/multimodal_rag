# 🚀 Multimodal RAG Chatbot

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-v1-green?style=for-the-badge)
![Qdrant](https://img.shields.io/badge/Qdrant-VectorDB-red?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM-black?style=for-the-badge)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-yellow?style=for-the-badge)

</p>

---

## 📖 Overview

A **production-style Multimodal Retrieval-Augmented Generation (RAG)** application that enables users to upload PDF documents, build a searchable knowledge base, and interact with the content using natural language.

Unlike traditional RAG systems, this project supports **multimodal document understanding** by processing:

- 📄 Text
- 📊 Tables
- 🖼 Images
- 📝 Image Captions

The application retrieves the most relevant information from the indexed documents and generates accurate responses using **Groq LLMs** while displaying document sources for transparency.

---

# ✨ Features

## 📂 Document Upload

- Upload PDF documents
- Manual indexing
- Prevent duplicate uploads

---

## 📚 Multimodal Ingestion

The ingestion pipeline extracts

- Text
- Tables
- Images

Images are automatically captioned using a Vision LLM to make visual information searchable.

---

## 🔎 Semantic Retrieval

- HuggingFace Embeddings
- Qdrant Vector Database
- Similarity Search
- Source Tracking

---

## 🤖 AI Chat

- Groq LLM
- Conversation Memory
- Source Citations
- Streaming-style UI

---

## 🖥 Streamlit Frontend

- Modern Chat Interface
- PDF Management
- Knowledge Base Indexing
- Delete Documents
- Reset Chatbot

---

# 🏗 Architecture

```
                   User

                     │

                     ▼

              Streamlit UI

                     │

                     ▼

               FastAPI Backend

        ┌────────────┼────────────┐
        ▼            ▼            ▼

   PDF Upload     Chat API     Admin API

        │

        ▼

   Multimodal Ingestion

        │

        ▼

Text │ Tables │ Images

        │

        ▼

 Vision Caption Generation

        │

        ▼

Chunking & Embeddings

        │

        ▼

      Qdrant Vector DB

        │

        ▼

 Semantic Retrieval

        │

        ▼

      Groq LLM

        │

        ▼

    Final Response
```

---

# 🧠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| Framework | LangChain v1 |
| Vector Database | Qdrant |
| Embeddings | HuggingFace |
| LLM | Groq |
| PDF Parsing | Unstructured |
| Vision | Groq Vision |
| Chunking | Recursive Text Splitter |

---

# 📂 Project Structure

```
multimodal_rag/

│

├── app/

│   ├── api/

│   ├── chains/

│   ├── embeddings/

│   ├── ingestion/

│   ├── llm/

│   ├── memory/

│   ├── retriever/

│   ├── vectorstore/

│   ├── config.py

│   └── main.py

│

├── tests/

├── streamlit_app.py

├── pyproject.toml

├── README.md

└── .gitignore
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/multimodal-rag.git

cd multimodal-rag
```

Install dependencies

```bash
uv sync
```

or

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file

```env
GROQ_API_KEY=

GROQ_MODEL=

QDRANT_URL=

QDRANT_API_KEY=

QDRANT_COLLECTION=
```

---

# ▶ Running the Backend

```bash
uvicorn app.main:app --reload
```

FastAPI

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# ▶ Running Streamlit

```bash
streamlit run streamlit_app.py
```

Open

```
http://localhost:8501
```

---

# 🚀 Workflow

```
Upload PDF

↓

Index Knowledge Base

↓

Generate Embeddings

↓

Store in Qdrant

↓

Ask Questions

↓

Semantic Retrieval

↓

Groq LLM

↓

Answer + Sources
```

---

# 📡 API Endpoints

## Upload

```
POST /upload
```

Upload a PDF.

---

## Index

```
POST /index
```

Index uploaded PDFs.

---

## Chat

```
POST /chat
```

Ask questions about indexed documents.

---

## Delete PDF

```
DELETE /admin/pdf/{filename}
```

Deletes

- PDF
- Images
- Vectors

---

## Reset

```
POST /admin/reset
```

Resets

- Uploaded PDFs
- Images
- Chat Memory
- Vector Database

---

# 🎯 Future Improvements

- Hybrid Search (BM25 + Dense Retrieval)
- Cross Encoder Reranking
- Agentic RAG
- Multi-user Sessions
- Authentication
- Docker Deployment
- Kubernetes
- CI/CD
- Redis Memory
- OCR Support
- Audio & Video RAG

---

# 📸 Screenshots

> Add screenshots of:

- Streamlit Home
- Upload PDF
- Chat
- Source Citations
- Swagger API

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📜 License

This project is released under the MIT License.

---

# 👨‍💻 Author

**Abdul Haq**

AI Engineer | Generative AI | RAG | LangChain | FastAPI | Streamlit

If you found this project useful, consider giving it a ⭐ on GitHub.
