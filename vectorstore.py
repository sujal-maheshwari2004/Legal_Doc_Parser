from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

def create_vectorstore(chunks):
    """
    Creates a FAISS vectorstore using the provided text chunks and Ollama embeddings model.
    """
    embeddings_model = OllamaEmbeddings(model="llama3")
    vectorstore = FAISS.from_texts(chunks, embedding=embeddings_model)
    return vectorstore, chunks
