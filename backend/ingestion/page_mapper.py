import fitz


def map_pages(pdf_path, hierarchy):

    print("[PAGE MAP] mapping TOC pages to PDF pages")

    doc = fitz.open(pdf_path)
    total_pages = len(doc)

    mapped = []

    for i, entry in enumerate(hierarchy):

        start = entry["page"]

        if i + 1 < len(hierarchy):
            next_page = hierarchy[i + 1]["page"]
            end = max(start, next_page - 1)
        else:
            end = total_pages

        mapped.append(
            {
                "chapter": entry.get("chapter"),
                "title": entry["title"],
                "level": entry["level"],
                "page_start": start,
                "page_end": end
            }
        )

    print("[PAGE MAP] mapped topics:", len(mapped))
    print("[DEBUG] Mapped sample:", mapped[0:5])
    return mapped