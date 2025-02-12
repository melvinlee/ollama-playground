import streamlit as st
from langchain_ollama import ChatOllama

# Define available models
AVAILABLE_MODELS = [
    "deepseek-r1:7b",
    "llama3.2:1b",
    "llama3.2:3b",
]

url = "http://localhost:11434"

st.title("Create GPT like Chatbot with Ollama🧠 and Langchain⚡!")

# Move model selection to sidebar
with st.sidebar:
    selected_model = st.selectbox("Select a model:", AVAILABLE_MODELS)
    st.markdown("Select different models to compare their responses. Make sure you have pulled the models using `ollama pull <model_name>` first.*")
    
    # Add the GitHub link at the bottom of the sidebar
    st.markdown("<br>" * 10, unsafe_allow_html=True)  # Add vertical spacing
    st.markdown(
        """<div style='position: fixed; bottom: 20px;'>
        <a href='https://github.com/melvinlee/ollama-playground' target='_blank'>
        https://github.com/melvinlee/ollama-playground
        </a></div>""", 
        unsafe_allow_html=True
    )

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat messages from history on app rerun
for chat_history in st.session_state.chat_history:
    with st.chat_message(chat_history["role"]):
        st.markdown(chat_history["content"])

def generate_response(text):
    llm = ChatOllama(model=selected_model, base_url=url, temperature=0)
    return llm.stream(text)

if prompt := st.chat_input("Say something"):
    st.chat_message("user").markdown(prompt)

    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(generate_response(prompt))
    # Add assistant response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})