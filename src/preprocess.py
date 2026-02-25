import nltk
import re
from nltk.corpus import stopwords

nltk.download("stopwords")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s₹]", "", text)
    tokens = text.split()

    stop_words = set(stopwords.words("english"))
    tokens = [t for t in tokens if t not in stop_words]

    cleaned_text = " ".join(tokens)

    return cleaned_text