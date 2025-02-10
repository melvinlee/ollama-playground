import streamlit as st
from langchain_ollama import ChatOllama

st.title("Create Chat Application with Ollama🧠 and Langchain⚡!")

st.write("https://github.com/melvinlee/ollama-playground")

with st.form("main-form"):
    text = st.text_input("Enter your text or question here:")
    submit = st.form_submit_button("Submit")

