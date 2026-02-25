# 📄 Document Intelligence System

An AI-powered document processing platform that automatically extracts text, classifies documents, summarizes content, and identifies key information such as names, dates, invoice numbers, and amounts using OCR and NLP techniques.

This system helps organizations digitize and understand documents quickly, reducing manual effort and improving efficiency.

---

## 🚀 Features

- 📤 **Document Upload**  
  Upload scanned documents and images  
  Supports invoices, forms, and receipts  

- 🔍 **OCR Text Extraction**  
  Converts images to machine-readable text  
  Handles printed documents with high accuracy  

- 🧹 **Text Preprocessing**  
  Cleans and normalizes extracted text  
  Removes noise and unnecessary symbols  

- 📄 **Document Classification**  
  Automatically detects document type  
  Categories: Invoice, Form, Receipt, etc.  

- 📝 **Text Summarization**  
  Generates concise document summaries  
  Highlights important content  

- 🏷️ **Named Entity Recognition (NER)**  
  Extracts key fields such as:  
  - Names  
  - Dates  
  - Amounts  
  - Invoice Numbers  
  - Organization Names  

- 📊 **Smart Key-Value Panel**  
  Displays extracted information in readable format  
  Helps users quickly understand documents  

- 🌐 **Interactive Web Interface**  
  User-friendly dashboard using Streamlit  
  Real-time document analysis  

---

## 🛠️ Tech Stack

### Frontend / UI
- Streamlit  
- HTML/CSS (via Streamlit components)  

### Backend / Processing
- Python  
- OpenCV  
- EasyOCR / Tesseract OCR  

### Machine Learning & NLP
- Scikit-learn  
- TF-IDF Vectorizer  
- Logistic Regression  
- spaCy  
- Regular Expressions (Regex)  

### Tools
- Git & GitHub  
- VS Code  
- Virtual Environment (venv)  

---

## 🗂️ Project Structure

  ```bash
  Document_Intelligence_System/
  │
  ├── data/
  │   ├── raw/
  │   └── processed/
  │
  ├── models/
  │   ├── train_classifier.py
  │   └── classifier_model.pkl
  │
  ├── src/
  │   ├── ocr_extract.py
  │   ├── preprocess.py
  │   ├── classify.py
  │   ├── summarize.py
  │   ├── ner_extract.py
  │   └── utils.py
  │
  ├── ui/
  │   └── app.py
  │
  └── requirements.txt
  ```

---

## 🔍 Key Modules

| Module | Description |
|--------|-------------|
| OCR | Extracts text from scanned documents using OCR engines |
| Preprocessing | Cleans and normalizes extracted text |
| Classification | Identifies document type using ML models |
| Summarization | Generates concise document summaries |
| NER | Extracts entities like names, dates, and amounts |
| UI | Displays results using Streamlit |

---

## 🧪 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-link>
cd Document_Intelligence_System
```
### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run ui/app.py
```
### Open your browser and go to:

```bash
http://localhost:8501
```
---

## 📊 Model Training

The document classification model is trained using machine learning techniques on labeled document datasets.

### Training Approach

- Text features are extracted using TF-IDF Vectorizer.
- A Logistic Regression classifier is used for document classification.
- The model is trained using FUNSD and SROIE datasets.
- Training includes both training and testing samples for better generalization.

### Training Steps

1. Prepare the dataset inside the data folder.
2. Preprocess the extracted OCR text.
3. Convert text into numerical features using TF-IDF.
4. Train the classifier using Logistic Regression.
5. Save the trained model for future predictions.

The trained model is stored as:

```bash
models/classifier_model.pkl
```

To retrain the model, run:

```bash
python models/train_classifier.py
```

---

## 📈 Results

- The system accurately classifies invoices, forms, and receipts.
- Named entities such as dates, names, and invoice numbers are extracted effectively.
- The summarization module generates meaningful document summaries.
- The application processes documents in real time.

---

## 🏁 Future Improvements

- Add support for handwritten document recognition.
- Implement multilingual document processing.
- Integrate advanced deep learning models.
- Enable cloud-based deployment.
- Improve user dashboard with analytics.
- Support bulk document uploads.

---

## 📚 Learning Outcomes

- Practical understanding of OCR and NLP pipelines.
- Experience in building end-to-end AI systems.
- Knowledge of machine learning model training.
- Exposure to real-world document automation.
- Improved software development practices.

---

## 🎓 Academic Context

This project was developed as part of a **B.Tech 5th Semester End-Term Project** and demonstrates practical implementation of:

- Machine Learning  
- Natural Language Processing (NLP)  
- Optical Character Recognition (OCR)  
- Web-based AI Applications  

It reflects the application of theoretical concepts to real-world document automation problems.

---
## 🧑‍💻 Author

Gummadi Balaram  
B.Tech Computer Science  
Document Intelligence System Project












