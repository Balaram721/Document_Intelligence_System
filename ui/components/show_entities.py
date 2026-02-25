import streamlit as st

def render_entities(entities):
    st.subheader("🔎 Named Entity Extraction")
    st.json(entities)