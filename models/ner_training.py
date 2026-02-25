import spacy
from spacy.tokens import DocBin

# Load base model
nlp = spacy.load("en_core_web_sm")

# Custom training data
TRAIN_DATA = [
    ("Invoice from Amazon totaling ₹5600 on 13-09-2025", {"entities":[(14,20,"ORG"),(30,35,"MONEY"),(39,49,"DATE")]}),
    ("Google salary receipt amounting USD 1200", {"entities":[(0,6,"ORG"),(33,42,"MONEY")]}),
]

# Add NER to pipeline
ner = nlp.get_pipe("ner")

# Add labels
for _, annotations in TRAIN_DATA:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# Training
nlp.begin_training()

for itn in range(20):
    random.shuffle(TRAIN_DATA)
    losses = {}
    for text, annotations in TRAIN_DATA:
        nlp.update([ (text, annotations) ], losses=losses)
    print(losses)

nlp.to_disk("models/ner_model")
print("✔ Custom NER model trained & saved.")