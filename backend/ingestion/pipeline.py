from backend.ingestion.toc_parser import extract_toc
from backend.ingestion.hierarchy_detector import detect_hierarchy
from backend.ingestion.page_mapper import map_pages
from backend.ingestion.text_extractor import extract_text_ranges
from backend.ingestion.cleaner import clean_text
from backend.ingestion.chunker import chunk_text

from backend.models.database import SessionLocal
from backend.models.topic import Topic
from backend.embeddings.embedder import embed_text
from backend.vector.qdrant_client import init_collection, insert_vectors

def run_pipeline(pdf_path):

    print("[PIPELINE] Starting ingestion pipeline")

    # -------- TOC --------
    toc = extract_toc(pdf_path)
    print("[PIPELINE] TOC sample:", toc[:10])
    print("[PIPELINE] TOC entries:", len(toc))

    # -------- Hierarchy --------
    hierarchy = detect_hierarchy(toc)
    print("[PIPELINE] Hierarchy levels detected")

    # -------- Page Mapping --------
    mapped = map_pages(pdf_path, hierarchy)
    print("[PIPELINE] Page ranges mapped:", len(mapped))

    # -------- Text Extraction --------
    extracted = extract_text_ranges(pdf_path, mapped)
    print("[PIPELINE] Text extraction complete")

    # -------- Cleaning --------
    cleaned = clean_text(extracted)
    print("[PIPELINE] Text cleaned")
    print("[DEBUG] Cleaned sample:",cleaned[0])

    # -------- Chunking --------
    chunks = chunk_text(cleaned)
    print("[PIPELINE] Chunking complete:", len(chunks))

    # -------- Save Topics --------
    print("[PIPELINE] Saving topics to database")

    db = SessionLocal()

    current_chapter = None
    saved_topics = 0

    for item in mapped:

        title = item["title"].strip()

        print("[PIPELINE] processing:", title)

        if title.lower().startswith("chapter"):
            current_chapter = title
            print("[PIPELINE] detected chapter:", current_chapter)
            continue

        skip_words = [
            "works cited",
            "recommended",
            "acknowledgements",
            "acknowledgments",
            "index",
            "bibliography"
        ]

        if any(word in title.lower() for word in skip_words):
            print("[PIPELINE] skipping reference section:", title)
            continue

        if current_chapter is None:
            print("[PIPELINE] skipping (no chapter yet):", title)
            continue

        topic = Topic(
            chapter=current_chapter,
            topic=title,
            subtopic=None,
            page_start=item["page_start"],
            page_end=item["page_end"],
            document_id=1
        )

        db.add(topic)
        saved_topics += 1

        print("[PIPELINE] saved topic:", title)

    db.commit()
    db.close()

    print("[PIPELINE] Topics saved to database:", saved_topics)


    # -------- Vector DB --------
    print("[PIPELINE] Initializing vector database")

    init_collection()

    print("[PIPELINE] Generating embeddings")

    texts = [c["text"] for c in chunks]

    vectors = embed_text(texts)

    payloads = []

    for c in chunks:
        payloads.append({
            "chapter": c.get("chapter"),
            "title": c["title"],
            "text": c["text"],
            "page_start": c.get("page_start"),
            "page_end": c.get("page_end")
        })

    print("[PIPELINE] Inserting vectors")

    insert_vectors(vectors, payloads)

    print("[PIPELINE] Vector storage complete")

    return chunks