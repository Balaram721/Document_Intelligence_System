import streamlit as st
from src.qa_module import answer_question

def render_qa(raw_text, entities):
    st.subheader("❓ Ask a Question")

    user_q = st.text_input("Enter your question:")

    if user_q:
        answer = answer_question(user_q, raw_text, entities)
        st.success(f"Answer: {answer}")