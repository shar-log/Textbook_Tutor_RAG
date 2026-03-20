from fastapi import APIRouter
from backend.models.database import SessionLocal
from backend.models.topic import Topic

router = APIRouter()


@router.get("/toc")
def get_toc():

    db = SessionLocal()

    topics = db.query(Topic).all()

    toc = {}

    for t in topics:

        if t.chapter not in toc:
            toc[t.chapter] = []

        toc[t.chapter].append(
            {
                "id": t.id,
                "title": t.topic,
                "page_start": t.page_start,
                "page_end": t.page_end
            }
        )

    db.close()

    result = []

    for chapter, topics in toc.items():
        result.append(
            {
                "chapter": chapter,
                "topics": topics
            }
        )

    return result