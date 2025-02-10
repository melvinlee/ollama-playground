url = "http://localhost:11434"
base_model = "llama3.2:3b"

import streamlit as st
from langchain_ollama import ChatOllama

st.title("Create Chat Application with Ollama🧠 and Langchain⚡!")

st.write("https://github.com/melvinlee/ollama-playground")

with st.form("main-form"):
    text = st.text_area("Enter your text or question here:", placeholder="Type your message...", label_visibility="collapsed", height=150)
    cols = st.columns([6, 1])
    with cols[1]:
        submit = st.form_submit_button("Send ➤", use_container_width=True)

def generate_response(text):
    llm = ChatOllama(model=base_model, base_url=url, temperature=0)
    return llm.stream(text)

if submit and text:
    # Create a container for the streaming response
    response_container = st.empty()
    full_response = ""
    
    # Stream the response
    with st.spinner("Generating response..."):
        for chunk in generate_response(text):
            full_response += chunk.content
            # Update the response container with accumulated text
            response_container.markdown(full_response + "▌")
        
        # Update final response without cursor
        response_container.markdown("")
        
        # Add to chat history
        st.session_state['chat_history'].append({
            "user": text, 
            "ollama": full_response
        })

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Create two columns for the history header
col1, col2 = st.columns([8, 1])
with col1:
    st.write("Chat History")
with col2:
    if st.button("🗑️", help="Clear chat history"):
        st.session_state.chat_history = []
        st.rerun()

for chat in st.session_state.chat_history:
    st.write(f"**🧑 User**: {chat['user']}")
    st.write(f"**🧠 Assistant**: {chat['ollama']}")
    st.write("---")