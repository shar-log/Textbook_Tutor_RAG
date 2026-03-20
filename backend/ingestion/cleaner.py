import re


def clean_text(extracted):

    print("[CLEAN] cleaning text")

    cleaned = []

    for item in extracted:

        text = item["text"]

        text = re.sub(r"\s+", " ", text)

        text = text.replace("- ", "")

        cleaned.append(
            {
                "chapter": item.get("chapter"),
                "title": item["title"],
                "text": text,
                "page_start": item.get("page_start"),
                "page_end": item.get("page_end")
            }
        )

    print("[CLEAN] cleaned items:", len(cleaned))

    return cleaned