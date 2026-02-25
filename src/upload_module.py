def upload_document(file):
    if not file:
        return None, "No file uploaded"

    allowed_extensions = ["pdf", "png", "jpg", "jpeg"]
    ext = file.name.split(".")[-1].lower()

    if ext not in allowed_extensions:
        return None, "Unsupported file format"

    return file, "File uploaded successfully"