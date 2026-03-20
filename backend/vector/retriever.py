from backend.vector.qdrant_client import client
from backend.config import QDRANT_COLLECTION
from backend.embeddings.embedding_service import model


def retrieve_chunks(query, top_k=5):

    print("[RETRIEVAL] Query:", query)

    query_vector = model.encode(query, normalize_embeddings=True)

    #results = client.search(
    results = client.query_points(
        collection_name=QDRANT_COLLECTION,
        query=query_vector,
        limit=top_k
    )

    chunks = []

    for r in results.points:
        chunks.append({
            "score": r.score,
            "chapter": r.payload.get("chapter"),
            "title": r.payload["title"],
            "page_start": r.payload.get("page_start"),
            "page_end": r.payload.get("page_end"),
            "text": r.payload["text"]
        })

    print("[RETRIEVAL] Retrieved:", len(chunks))

    return chunks