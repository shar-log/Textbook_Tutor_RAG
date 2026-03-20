from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from backend.config import QDRANT_DIR, QDRANT_COLLECTION, EMBEDDING_DIM

print("[QDRANT] Starting local vector database")

client = QdrantClient(path=QDRANT_DIR)


def init_collection():

    print("[QDRANT] Creating collection")

    client.recreate_collection(
        collection_name=QDRANT_COLLECTION,
        vectors_config=VectorParams(
            size=EMBEDDING_DIM,
            distance=Distance.COSINE
        )
    )

    print("[QDRANT] Collection ready")


def insert_vectors(vectors, payloads):

    print("[QDRANT] inserting vectors:", len(vectors))

    points = []

    for i, vector in enumerate(vectors):

        points.append(
            PointStruct(
                id=i,
                vector=vector.tolist(),
                payload=payloads[i]
            )
        )

    client.upsert(
        collection_name=QDRANT_COLLECTION,
        points=points
    )

    print("[QDRANT] vectors inserted")