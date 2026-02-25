import streamlit as st

def render_summary(summary):
    st.subheader("📝 Document Summary")
    st.write(summary)