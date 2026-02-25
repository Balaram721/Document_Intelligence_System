def preview_text(text, limit=500):
    return text[:limit] + "..." if len(text) > limit else text