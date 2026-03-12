import streamlit as st
import tempfile

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama

st.title("AI Research Assistant")

uploaded_file = st.file_uploader("Upload a research paper (PDF)", type="pdf")

if uploaded_file:

    # Save uploaded file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split text into chunks
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    docs = text_splitter.split_documents(documents)

    # Create embeddings
    embeddings = OllamaEmbeddings(model="llama3")

    # Create vector database
    vectorstore = FAISS.from_documents(docs, embeddings)

    # Create retriever
    retriever = vectorstore.as_retriever()

    # Load LLM
    llm = Ollama(model="llama3")

    # Question input
    query = st.text_input("Ask a question about the paper")

    if query:

        relevant_docs = retriever.invoke(query)

        context = "\n\n".join([doc.page_content for doc in relevant_docs])

        prompt = f"""
        Answer the question using the context below.

        Context:
        {context}

        Question:
        {query}
        """

        response = llm.invoke(prompt)

        st.write(response)