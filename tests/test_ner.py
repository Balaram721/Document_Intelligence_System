from src.ner_extract import extract_entities

def test_ner():
    text = "Invoice from Amazon on 13/08/2023 with total ₹6700"
    ents = extract_entities(text)
    assert "₹6700" in ents.get("MONEY", [""])
    assert "13/08/2023" in ents.get("DATE", [""])
    print("✔ NER test passed:", ents)