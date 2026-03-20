from backend.vector.qdrant_client import client
from backend.config import QDRANT_COLLECTION
from qdrant_client.models import Filter, FieldCondition, MatchValue


def retrieve_topic_chunks(topic, top_k=8):

    print("[TOPIC RETRIEVAL] Topic:", topic.topic)

    results = client.scroll(
        collection_name=QDRANT_COLLECTION,
        scroll_filter=Filter(
            must=[
                FieldCondition(
                    key="title",
                    match=MatchValue(value=topic.topic)
                )
            ]
        ),
        limit=top_k
    )

    chunks = []

    for r in results[0]:

        payload = r.payload

        chunks.append({
            "chapter": payload.get("chapter"),
            "title": payload["title"],
            "page_start": payload.get("page_start"),
            "page_end": payload.get("page_end"),
            "text": payload["text"],
            "score": 1.0
        })

    print("[TOPIC RETRIEVAL] Chunks:", len(chunks))

    return chunks