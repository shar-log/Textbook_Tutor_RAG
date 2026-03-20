import os

# ==========================
# PROJECT ROOT
# ==========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "..", "data")
UPLOAD_DIR = os.path.join(DATA_DIR, "uploads")
QDRANT_DIR = os.path.join(DATA_DIR, "qdrant")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(QDRANT_DIR, exist_ok=True)

# ==========================
# DATABASE
# ==========================

DATABASE_URL = "sqlite:///./textbook_tutor.db"

# ==========================
# EMBEDDINGS
# ==========================

EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"
EMBEDDING_DIM = 768

# ==========================
# CHUNKING
# ==========================

CHUNK_MIN_TOKENS = 500
CHUNK_MAX_TOKENS = 1000

# ==========================
# VECTOR DATABASE
# ==========================

QDRANT_COLLECTION = "textbook_chunks"

# ==========================
# LLM
# ==========================

OLLAMA_URL = "http://localhost:11434/api/generate"
LLM_MODEL = "mistral"

# ==========================
# PIPELINE
# ==========================

TOC_SCAN_PAGES = 20
EMBED_BATCH_SIZE = 32