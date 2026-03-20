# 📘 Textbook Tutor (RAG-based AI)

An AI-powered textbook assistant that answers questions strictly from a given PDF using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- Semantic search using embeddings (BGE)
- Local vector DB (Qdrant)
- Strict textbook-only answers
- Fallback for out-of-scope questions
- Chat-based UI (Next.js)
- Source highlighting

---

## 🧠 Architecture

User Question  
→ Embedding  
→ Qdrant Retrieval  
→ LLM (Ollama)  
→ Answer  

---

## 🛠️ Tech Stack

- FastAPI (backend)
- Next.js (frontend)
- Qdrant (vector DB)
- Ollama (LLM)
- BGE Embeddings

---

## ⚙️ Setup

### Backend

```bash
cd backend
pip install -r ../requirements.txt
uvicorn main:app --reload