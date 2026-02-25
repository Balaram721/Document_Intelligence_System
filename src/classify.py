import os
import pickle

VEC_PATH = "models/vectorizer_funsd_sorie.pkl"
MODEL_PATH = "models/classifier_funsd_sorie.pkl"


if os.path.exists(VEC_PATH) and os.path.exists(MODEL_PATH):
    with open(VEC_PATH, "rb") as f:
        _vectorizer = pickle.load(f)
    with open(MODEL_PATH, "rb") as f:
        _clf = pickle.load(f)
else:
    _vectorizer = None
    _clf = None


def classify_document(text: str):
    global _vectorizer, _clf



    if _vectorizer is not None and _clf is not None:
        X = _vectorizer.transform([text])


        probs = _clf.predict_proba(X)[0]


        best_index = probs.argmax()
        pred_raw = _clf.classes_[best_index]
        confidence = probs[best_index] * 100


        if pred_raw == "FORM":
            pred = "Form / Application"
        elif pred_raw == "RECEIPT":
            pred = "Receipt / Invoice"
        else:
            pred = pred_raw

        return pred, confidence


    t = text.lower()
    if "invoice" in t or "receipt" in t or "gst" in t:
        return "Invoice / Receipt", 80.0
    if "form" in t or "application" in t:
        return "Form / Application", 75.0

    return "General Document", 60.0