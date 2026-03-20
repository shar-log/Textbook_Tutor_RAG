from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.lesson_service import generate_lesson

router = APIRouter()


class LessonRequest(BaseModel):
    topic_id: int
    kid_mode: bool = False


@router.post("/lesson")
def lesson(req: LessonRequest):

    print("[API] Lesson request:", req.topic_id)

    result = generate_lesson(req.topic_id, req.kid_mode)

    return result