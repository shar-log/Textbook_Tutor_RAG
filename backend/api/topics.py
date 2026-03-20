from fastapi import APIRouter
from backend.models.database import SessionLocal
from backend.models.topic import Topic

router = APIRouter()

@router.get("/topics")
def get_topics():

    db = SessionLocal()

    topics = db.query(Topic).all()

    results = []

    for t in topics:
        results.append({
            "id": t.id,
            "title": t.topic,
            "chapter": t.chapter,
            "page_start": t.page_start,
            "page_end": t.page_end
        })

    db.close()

    return results