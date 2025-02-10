## Running the Application

Start Ollama server (in a separate terminal):
```bash
ollama serve
```

Pull the model (first time only):
```bash
ollama pull llama2:3b
```

Start the Streamlit app:
```bash
cd chatbot
pipenv run streamlit run app.py
```

The application will be available at `http://localhost:8501`