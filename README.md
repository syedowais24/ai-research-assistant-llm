# AI Research Assistant (LLM)

An AI-powered research assistant that allows users to upload research papers (PDF) and ask questions about them.
The system uses **Retrieval-Augmented Generation (RAG)** with **Llama3 via Ollama**, **FAISS vector search**, and **Streamlit** to generate answers from the document content.

---

## Features

* Upload research papers in **PDF format**
* Automatic **text extraction from PDFs**
* **Semantic search** using FAISS vector database
* **Retrieval-Augmented Generation (RAG)**
* Ask questions and get **context-aware answers**
* Simple **Streamlit web interface**
* Uses **Llama3 locally with Ollama**

---

## Tech Stack

* Python
* Streamlit
* LangChain
* FAISS
* Ollama (Llama3)
* PyPDF
* Tiktoken

---

## Project Structure

```
ai-research-assistant-llm
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/syedowais24/ai-research-assistant-llm.git
cd ai-research-assistant-llm
```

---

### 2. Create virtual environment (recommended)

Linux / Mac:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download Ollama:

https://ollama.com

Pull the **Llama3 model**:

```bash
ollama pull llama3
```

Make sure Ollama is running.

---

## Run the Application

```bash
streamlit run app.py
```

Open your browser:

```
http://localhost:8501
```

---

## How It Works

1. User uploads a research paper (PDF)
2. Text is extracted from the document
3. Text is split into smaller chunks
4. Chunks are converted into **vector embeddings**
5. Embeddings are stored in **FAISS vector database**
6. When a question is asked:

   * Relevant chunks are retrieved
   * Llama3 generates an answer using the retrieved context

This technique is called **Retrieval-Augmented Generation (RAG)**.

---

## Example Questions

```
What is the main contribution of this paper?
```

```
Summarize the methodology used in the research.
```

```
What are the limitations mentioned in the paper?
```

---

## Requirements

* Python 3.9+
* Ollama installed
* Llama3 model downloaded
* Internet connection for installing packages

---

## Future Improvements

* Multi-document support
* Chat history
* Citation highlighting
* Research paper summarization
* Export answers to Markdown or PDF
* Persistent vector database

---

## License

This project is open-source and available under the MIT License.

---

## Author

**Syed Owais**

GitHub:
https://github.com/syedowais24
