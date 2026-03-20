import fitz
import re
from backend.config import TOC_SCAN_PAGES


def extract_toc(pdf_path):

    print("[TOC] scanning first", TOC_SCAN_PAGES, "pages")

    doc = fitz.open(pdf_path)

    toc_entries = []

    for page_num in range(min(TOC_SCAN_PAGES, len(doc))):

        page = doc.load_page(page_num)
        text = page.get_text()

        lines = text.split("\n")

        for line in lines:

            line = line.strip()

            if not line:
                continue

            # Match TOC lines ending with page numbers
            match = re.search(r"(.+?)\s+(\d{1,4})$", line)

            if not match:
                continue

            title = match.group(1).strip()
            page_number = int(match.group(2))

            # Clean leader characters
            title = re.sub(r"[._]{3,}", "", title)
            title = re.sub(r"_+", "", title)
            title = re.sub(r"\s+", " ", title).strip()

            # remove TOC artifacts
            if "contents" in title.lower():
                continue

            # Remove obvious noise
            if len(title) < 3:
                continue

            if title.lower().startswith(("figure", "table", "appendix")):
                continue

            if "printing" in title.lower():
                continue

            # Detect hierarchy
            if re.match(r"chapter\s+\d+", title.lower()):
                level = 0
            elif re.match(r"\d+\.\d+\.\d+", title):
                level = 3
            elif re.match(r"\d+\.\d+", title):
                level = 2
            elif re.match(r"\d+\.", title):
                level = 1
            else:
                level = 1

            print("[TOC] parsed:", title, "| level:", level, "| page:", page_number)

            toc_entries.append({
                "title": title,
                "page": page_number,
                "level": level
            })

    print("[TOC] entries detected:", len(toc_entries))

    return toc_entries