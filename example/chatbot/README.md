## Prerequisites

- [Devbox](https://www.jetpack.io/devbox)
- [Ollama](https://ollama.ai)

Enter development shell:
```bash
devbox shell
```

Install Python dependencies:
```bash
pipenv install
```

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
pipenv run streamlit run app.py
```

The application will be available at `http://localhost:8501`