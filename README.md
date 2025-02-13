# ollama-playground [![Built with Devbox](https://jetpack.io/img/devbox/shield_moon.svg)](https://jetpack.io/devbox/docs/contributor-quickstart/)

Experiment with Ollama and LangChain.



## Prerequisites

- [Devbox](https://www.jetpack.io/devbox)
- [Ollama](https://ollama.ai)

Enter development shell:
```bash
devbox shell
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
devbox run start-chatgpt
```

The application will be available at `http://localhost:8501`