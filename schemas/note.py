def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item.get("title", ""),
        "desc": item.get("desc", ""),
        "important": bool(item.get("important", False)),
    }


def notesEntity(items) -> list[dict]:
    return [noteEntity(item) for item in items]
