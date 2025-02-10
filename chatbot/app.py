url = "http://localhost:11434"
base_model = "llama3.2:3b"

import streamlit as st
from langchain_ollama import ChatOllama

st.title("Create Chat Application with Ollama🧠 and Langchain⚡!")

st.write("https://github.com/melvinlee/ollama-playground")

with st.form("main-form"):
    text = st.text_input("Enter your text or question here:")
    submit = st.form_submit_button("Submit")

def generate_response(text):
    llm = ChatOllama(model=base_model, base_url=url, temperature=0)
    response = llm.invoke(text)
    return response.content

if submit and text:
    with st.spinner("Generating response..."):
        response = generate_response(text)
        st.session_state['chat_history'].append({"user": text, "ollama": response})
        st.write(response)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.write("Chat History")

for chat in st.session_state.chat_history:
    st.write(f"**🧑 User**: {chat['user']}")
    st.write(f"**🧠 Assistant**: {chat['ollama']}")
    st.write("---")