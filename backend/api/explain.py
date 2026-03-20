from fastapi import APIRouter
from backend.services.explanation_service import explain_topic
from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str

router = APIRouter()

@router.post("/explain")
def explain(req: QuestionRequest):

    print("[API] Explain request:", req.question)

    result = explain_topic(req.question)

    return result