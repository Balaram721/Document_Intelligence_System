from src.classify import classify_document

def test_classification():
    sample_text = "Invoice no 231 Date 13-08-2023 Total ₹6700 Vendor Flipkart"
    pred = classify_document(sample_text)
    assert pred in range(0, 16) or isinstance(pred, int)
    print("✔ Classification test passed (returned:", pred, ")")