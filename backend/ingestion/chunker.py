from backend.config import CHUNK_MAX_TOKENS

def chunk_text(cleaned):

    print("[CHUNKING] generating chunks")

    chunks = []

    for item in cleaned:

        text = item["text"]

        words = text.split()

        start = 0

        while start < len(words):

            end = start + CHUNK_MAX_TOKENS

            chunk_words = words[start:end]

            chunk_text = " ".join(chunk_words)
            
            #print("[CHUNKING] sample item:", item)

            chunks.append({
                "chapter": item.get("chapter"),
                "title": item.get("title"),
                "text": chunk_text,
                "page_start": item.get("page_start"),
                "page_end": item.get("page_end")
            })
            

            start = end

    print("[CHUNKING] total chunks:", len(chunks))

    return chunks