import fitz


def extract_text_ranges(pdf_path, mapped_topics):

    print("[TEXT] extracting text ranges")

    doc = fitz.open(pdf_path)

    results = []

    for topic in mapped_topics:

        text = ""

        for p in range(topic["page_start"], topic["page_end"] + 1):

            if p - 1 < len(doc):

                page = doc.load_page(p - 1)

                text += page.get_text()

        results.append(
            {
                "chapter": topic.get("chapter"),
                "title": topic["title"],
                "text": text,
                "page_start": topic.get("page_start"),
                "page_end": topic.get("page_end")
            }
        )

    print("[TEXT] topics extracted:", len(results))

    return results