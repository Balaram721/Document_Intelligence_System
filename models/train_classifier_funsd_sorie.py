import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

TRAIN_PATH = "data/raw/classifier_training/"

def load_training_text():
    data = []
    labels = []

    for filename in os.listdir(TRAIN_PATH):
        fpath = os.path.join(TRAIN_PATH, filename)
        if not fpath.endswith(".txt"):
            continue
        
        category = filename.replace(".txt", "")
        with open(fpath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            text = line.strip()
            if text:
                data.append(text)
                labels.append(category)

    return data, labels

def main():

    print(" LOADING CLASSIFIER TRAINING DATA ")
    X, y = load_training_text()

    print(" TF–IDF Vectorizing ")
    vectorizer = TfidfVectorizer(max_features=2500, ngram_range=(1,3))
    X_vec = vectorizer.fit_transform(X)

    print(" Training Logistic Regression ")
    clf = LogisticRegression(max_iter=4000)
    clf.fit(X_vec, y)

    print(" Saving Model ")
    with open("models/classifier_model.pkl", "wb") as f:
        pickle.dump(clf, f)

    with open("models/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    print("Training Completed Successfully!")

if __name__ == "__main__":
    main()