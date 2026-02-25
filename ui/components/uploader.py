import streamlit as st

def render_uploader():
    st.header("📤 Upload Your Document")

    uploaded = st.file_uploader(
        "Choose a file (PDF, PNG, JPG, JPEG)",
        type=["pdf", "png", "jpg", "jpeg"],
        key="main_uploader"
    )

    if uploaded is not None:
        st.success("File uploaded successfully.")
        return uploaded

    return None