from src.summarize import summarize_text

def test_summary():
    text = """
    This invoice was issued by Amazon on 13-08-2023.
    Total amount is ₹6700.
    Payment was done via credit card.
    The customer is John Doe.
    """
    summary = summarize_text(text)
    assert "invoice" in summary or "Amazon" in summary
    print("✔ Summary test passed:", summary)