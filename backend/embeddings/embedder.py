from sentence_transformers import SentenceTransformer

print("[EMBED] Loading embedding model")

model = SentenceTransformer("BAAI/bge-base-en-v1.5")


def embed_text(texts):

    print("[EMBED] generating embeddings:", len(texts))

    embeddings = model.encode(texts, normalize_embeddings=True)

    return embeddings