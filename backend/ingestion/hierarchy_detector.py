def detect_hierarchy(entries):

    print("[HIERARCHY] detecting levels")

    learning_units = []
    current_chapter = None
    for i, item in enumerate(entries):
        #chapter = item.get("chapter")
        title = item["title"]
        level = item["level"]
        #detect chapter
        if level == 0:
            current_chapter = title
        #attach chapter to item
        item["chapter"] = current_chapter
        # Always keep chapters
        if level == 0:
            learning_units.append(item)
            continue

        # Keep node if next level is not deeper
        if i + 1 < len(entries):
            next_level = entries[i + 1]["level"]

            if next_level <= level:
                learning_units.append(item)
        else:
            learning_units.append(item)

    print("[HIERARCHY] learning units:", len(learning_units))
    print("[DEBUG - HIERARCHY] Learning units sample:", learning_units[0:5])
    return learning_units