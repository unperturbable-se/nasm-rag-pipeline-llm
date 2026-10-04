
# Syntax-Specialized RAG Engine 

A Retrieval-Augmented Generation (RAG) backend designed to specialize Large Language Models on obscure, niche, or custom syntaxes and documentation. By grounding model responses in targeted local documentation chunks, this pipeline eliminates hallucinated syntax errors and forces precise code generation.

---

##  Purpose

General-purpose LLMs frequently produce hallucinated methods, invalid keywords, and broken syntax when writing code for niche frameworks, custom DSLs, or specific assembly dialects (e.g., NASM or specialized C++ libraries). This engine intercepts user queries, retrieves relevant documentation snippets via keyword and vector indexing, and injects clean context into the LLM prompt to enforce strict syntax accuracy.

---

## 🛠 Core Libraries & Dependencies

* **[LangChain](https://www.langchain.com/)**: Document loading, text splitting, chunking, and retriever pipeline orchestration.
* **[FastAPI](https://fastapi.tiangolo.com/)**: Asynchronous web framework serving the core inference and model-configuration endpoints.
* **[OpenAI Python SDK](https://github.com/openai/openai-python)**: Unified inference client for querying Groq and OpenAI-compatible API providers.
* **[MarkItDown](https://github.com/microsoft/markitdown)**: Utility for converting raw files and documents into clean, LLM-legible Markdown.
* **Standard Python Libraries (`urllib`, `re`, `bs4`)**: Web scraping and HTML parsing to strip useless boilerplates, ads, and noise before indexing.

---

## 📂 Backend Architecture


```

Backend/
├── main.py         # FastAPI endpoints & lifecycle management
├── rag_maker.py    # LangChain chunking, vector indexing, & retrieval logic
└── docs/           # Raw syntax documentation files

```

---

##  API Endpoints

### 1. `POST /query`
Accepts a user question, executes context retrieval over the indexed codebase documentation using the RAG pipeline, and returns a grounded response.

* **Payload:**
  ```json
  {
    "Query": "How do I render a texture?"
  }

```

* **Response:**
```json
{
  "Query": "How do I render a texture?",
  "Answer": "To render a texture..."
}

```



### 2. `POST /model_selection`

Dynamically changes or updates the underlying LLM provider, base URL, or target model at runtime.

* **Payload:**
```json
{
  "key": "gsk_...",
  "url": "[https://api.groq.com/openai/v1](https://api.groq.com/openai/v1)",
  "model": "openai/gpt-oss-120b"
}

```



##  Quick Start

### 1. Clone the Repository
Clone the repository along with all nested submodules:
```bash
git clone --recursive [https://github.com/unperturbable-se/nasm-rag-pipeline-llm.git](https://github.com/unperturbable-se/nasm-rag-pipeline-llm.git)
cd nasm-rag-pipeline-llm

```

### 2. Backend Setup

Navigate to the `Backend` directory, set up your Python virtual environment using `uv`, install dependencies, and launch the server:

```bash
cd Backend

# Create virtual environment and install requirements
uv venv
uv pip install -r requirements.txt

# Run backend.py via Uvicorn
uvicorn backend:app --reload --port 8000

```

### 3. Frontend Setup

1. Open `Frontend/index.html` using **Live Server** (or any static HTTP server) in your editor/browser.
2. Enter your API key directly into the settings panel in the browser user interface to begin asking questions.



