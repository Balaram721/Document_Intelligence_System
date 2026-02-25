from src.preprocess import clean_text

def test_cleaning():
    raw = "This is an Invoice from Amazon for ₹5600!!!"
    cleaned = clean_text(raw)
    assert "invoice" in cleaned
    assert "amazon" in cleaned
    assert "₹5600" in cleaned
    print("✔ Preprocessing test passed")