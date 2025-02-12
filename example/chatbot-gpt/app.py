import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate, ChatPromptTemplate

# Define available models
AVAILABLE_MODELS = [
    "deepseek-r1:7b",
    "llama3.2:1b",
    "llama3.2:3b",
]

url = "http://localhost:11434"

st.title("Create GPT like Chatbot with Ollama🧠 and Langchain⚡!")

system_message = SystemMessagePromptTemplate.from_template("You are a helpful AI Assistant")
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

def generate_response():
    model = ChatOllama(model=selected_model, base_url=url, temperature=0)

    chat_template = ChatPromptTemplate.from_messages(chat_history)
    chain = chat_template | model | StrOutputParser () 
    
    response = chain.stream({})

    return response

def get_history():
    chat_history =[system_message]
    
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            chat_history.append(HumanMessagePromptTemplate.from_template(chat["content"]))
        else:
            chat_history.append(AIMessagePromptTemplate.from_template(chat["content"]))
    return chat_history

if prompt := st.chat_input("Say something"):
    st.chat_message("user").markdown(prompt)

    st.session_state.chat_history.append({"role": "user", "content": prompt})

    humanPrompt = HumanMessagePromptTemplate.from_template(prompt)
    
    chat_history = get_history()
    chat_history.append(humanPrompt)

    print(chat_history)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(generate_response())
    # Add assistant response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})