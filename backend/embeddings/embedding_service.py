from sentence_transformers import SentenceTransformer
from backend.config import EMBEDDING_MODEL, EMBED_BATCH_SIZE

print("[EMBED] Loading embedding model:", EMBEDDING_MODEL)

model = SentenceTransformer(EMBEDDING_MODEL)


def generate_embeddings(chunks):

    print("[EMBED] Generating embeddings")

    texts = [c["text"] for c in chunks]

    embeddings = model.encode(
        texts,
        batch_size=EMBED_BATCH_SIZE,
        show_progress_bar=True
    )

    results = []

    for i, chunk in enumerate(chunks):

        results.append({
            "title": chunk["title"],
            "text": chunk["text"],
            "vector": embeddings[i]
        })

    print("[EMBED] Generated vectors:", len(results))

    return results