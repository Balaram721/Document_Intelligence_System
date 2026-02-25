import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image

def extract_text_from_document(file_obj):

    filename = file_obj.name.lower()


    if filename.endswith(".pdf"):
        pdf_bytes = file_obj.read()
        pages = convert_from_bytes(pdf_bytes)

        text = ""
        for page in pages:
            text += pytesseract.image_to_string(page) + "\n"

        return text.strip()

 
    else:
        img = Image.open(file_obj)
        text = pytesseract.image_to_string(img)
        return text.strip()