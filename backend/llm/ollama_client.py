import requests
from backend.config import OLLAMA_URL, LLM_MODEL


def generate_llm_response(prompt):

    print("[LLM] Sending prompt to Ollama")

    payload = {
        "model": LLM_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    data = response.json()

    print("[LLM] Response received")

    return data["response"]