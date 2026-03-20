from backend.models.database import SessionLocal
from backend.models.topic import Topic
from backend.vector.topic_retriever import retrieve_topic_chunks
from backend.llm.ollama_client import generate_llm_response


def generate_lesson(topic_id, kid_mode=False):

    db = SessionLocal()

    topic = db.query(Topic).filter(Topic.id == topic_id).first()

    db.close()

    if not topic:
        return {"error": "Topic not found"}

    print("[LESSON] Generating lesson for:", topic.topic)

    chunks = retrieve_topic_chunks(topic)

    context = "\n\n".join([c["text"] for c in chunks])

    if kid_mode:
        audience = "Explain like the student is 10 years old using simple language."
    else:
        audience = "Explain clearly for an adult learner."

    prompt = f"""
You are a textbook tutor.

Teach the topic using these sections:

Concept
Why it matters
Example
Analogy
Key takeaway

{audience}

TEXTBOOK CONTEXT
{context}

TOPIC
{topic.topic}
"""

    response = generate_llm_response(prompt)

    return {
        "lesson": response,
        "sources": chunks
    }