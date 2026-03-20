from backend.vector.retriever import retrieve_chunks
from backend.llm.ollama_client import generate_llm_response


def explain_topic(question):

    print("[EXPLAIN] Generating explanation")

    chunks = retrieve_chunks(question)

    context = "\n\n".join([c["text"] for c in chunks])
    
    prompt = f"""
You are a helpful teaching assistant.

Use the provided textbook context first.

If additional knowledge is used, label it clearly.

CONTEXT
{context}

QUESTION
{question}

Explain clearly for a student.
"""

    answer = generate_llm_response(prompt)

    return {
        "answer": answer,
        "sources": chunks
    }