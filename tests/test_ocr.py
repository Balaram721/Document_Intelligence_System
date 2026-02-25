import io
from src.ocr_extract import extract_text_from_document
from PIL import Image, ImageDraw

def test_ocr_on_generated_image():
    img = Image.new("RGB", (200, 60), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((10,10), "Hello World", fill=(0,0,0))

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)

    extracted_text = extract_text_from_document(buf)
    assert "Hello" in extracted_text
    print("✔ OCR test passed")