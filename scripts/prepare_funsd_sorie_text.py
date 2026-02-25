import os
import csv
from PIL import Image
import pytesseract

FUNSD_IMG_DIR = "data/raw/funsd/training_data/images"
SORIE_IMG_DIR = "data/raw/sroie/train"  # adjust name if needed
OUT_CSV = "data/processed/classification/funsd_sorie_text.csv"

os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)

def ocr_image(path):
    try:
        img = Image.open(path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        print(f"Error OCR-ing {path}: {e}")
        return ""

def collect_samples():
    rows = []

    # FUNSD → label: FORM
    for fname in os.listdir(FUNSD_IMG_DIR):
        if fname.lower().endswith((".png", ".jpg", ".jpeg")):
            full_path = os.path.join(FUNSD_IMG_DIR, fname)
            print("OCR FUNSD:", fname)
            text = ocr_image(full_path)
            if len(text) > 20:
                rows.append(["FORM", text])

    # SROIE → label: RECEIPT
    for fname in os.listdir(SORIE_IMG_DIR):
        if fname.lower().endswith((".png", ".jpg", ".jpeg", ".jpg")):
            full_path = os.path.join(SORIE_IMG_DIR, fname)
            print("OCR SROIE:", fname)
            text = ocr_image(full_path)
            if len(text) > 20:
                rows.append(["RECEIPT", text])

    return rows


if __name__ == "__main__":
    samples = collect_samples()
    print("Total samples:", len(samples))

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["label", "text"])
        writer.writerows(samples)

    print("Saved training data to:", OUT_CSV)