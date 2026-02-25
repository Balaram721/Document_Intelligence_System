import streamlit as st
from components.uploader import render_uploader
from components.display_text import render_raw_text, render_cleaned_text
from components.show_summary import render_summary
from components.show_entities import render_entities
from src.ocr_extract import extract_text_from_document
from src.preprocess import clean_text
from src.classify import classify_document
from src.summarize import summarize_text
from src.ner_extract import extract_entities
from src.smart_keypanel import generate_key_value_panel

st.set_page_config(
    page_title="Document Intelligence System",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("📄 Document Intelligence System")
st.write("Upload a document and let the AI read, classify, summarize, and analyze it.")
file = render_uploader()
if file:

    st.success(" Document successfully received!")
    st.markdown("---")
    st.header(" Step 1 — OCR Extraction")

    raw_text = extract_text_from_document(file)
    render_raw_text(raw_text)
    st.success(" OCR completed!")

    st.markdown("---")
    st.header(" Step 2 — Cleaning & Preprocessing Text")

    cleaned = clean_text(raw_text)
    render_cleaned_text(cleaned)
    st.success(" Preprocessing completed!")

    st.markdown("---")
    st.header(" Step 3 — Document Classification")

    doc_type, confidence = classify_document(cleaned)

    st.subheader(f" Predicted Document Type: **{doc_type}**")
    st.write(f" Confidence: {confidence:.2f}%")

    st.markdown("---")
    st.header(" Step 4 — Summarizing the Document")

    summary = summarize_text(raw_text)
    render_summary(summary)
    st.success(" Summarization completed!")

    st.markdown("---")
    st.header(" Step 5 — Extracting Key Fields / Entities")

    entities = extract_entities(raw_text)
    render_entities(entities)
    st.success(" Entity extraction done!")

    if raw_text and entities:
        st.subheader(" Extracted Key Information")

        keydata = generate_key_value_panel(entities,doc_type)

        for k, v in keydata.items():
            st.write(f"**{k}**: {v}")
else:
    st.info(" Please upload a document to begin.")