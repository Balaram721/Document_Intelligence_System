import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt")

def summarize_text(text, max_sentences=4):
    sentences = sent_tokenize(text)
    if len(sentences) <= max_sentences:
        return text

    word_freq = {}
    for word in text.split():
        word_freq[word] = word_freq.get(word, 0) + 1

    sentence_scores = {}
    for sentence in sentences:
        for word in sentence.split():
            if word in word_freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]

    ranked = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    summary = " ".join(ranked[:max_sentences])

    return summary