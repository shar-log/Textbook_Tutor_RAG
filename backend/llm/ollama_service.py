import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"


def generate_explanation(context, query):

    prompt = f"""
You are a helpful tutor explaining textbook content.

Use the textbook context below to answer the question.

If the answer is not in the context, say so.

Context:
{context}

Question:
{query}

Explain clearly in a teaching style.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()

    return result["response"]