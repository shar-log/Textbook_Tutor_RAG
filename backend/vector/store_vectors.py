from backend.vector.qdrant_client import client
from backend.config import QDRANT_COLLECTION


def store_embeddings(embedded_chunks):

    print("[QDRANT] Inserting vectors")

    points = []

    for i, item in enumerate(embedded_chunks):

        points.append({
            "id": i,
            "vector": item["vector"].tolist(),
            "payload": {
                "title": item["title"],
                "text": item["text"]
            }
        })

    client.upsert(
        collection_name=QDRANT_COLLECTION,
        points=points
    )

    print("[QDRANT] Stored vectors:", len(points))