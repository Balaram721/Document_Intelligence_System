from datasets import load_dataset
from transformers import LayoutLMv2ForTokenClassification, LayoutLMv2Processor, Trainer, TrainingArguments

# Load FUNSD dataset from Hugging Face
dataset = load_dataset("nielsr/funsd")

processor = LayoutLMv2Processor.from_pretrained("microsoft/layoutlmv2-base-uncased")
model = LayoutLMv2ForTokenClassification.from_pretrained(
    "microsoft/layoutlmv2-base-uncased",
    num_labels=7
)

def process_batch(example):
    encoded_inputs = processor(
        example["image"], 
        example["words"], 
        boxes=example["bbox"], 
        word_labels=example["ner_tags"], 
        padding="max_length", 
        truncation=True
    )
    return encoded_inputs

encoded_dataset = dataset.map(process_batch, batched=True)

training_args = TrainingArguments(
    output_dir="./models/layoutlm-funsd",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=5e-5,
    num_train_epochs=15,
    save_steps=200,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=encoded_dataset["train"],
    eval_dataset=encoded_dataset["test"]
)

trainer.train()