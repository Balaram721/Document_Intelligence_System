import streamlit as st

def render_raw_text(raw_text: str):
    st.subheader("🔍 OCR Text Extraction")
    st.text_area("Extracted Text", raw_text or "", height=200)

def render_cleaned_text(cleaned: str):
    st.subheader("🧹 Cleaned & Normalized Text")
    st.text_area("Processed Text", cleaned or "", height=200)