from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from config import CHROMA_DB_DIR, OLLAMA_BASE_URL, EMBEDDING_MODEL

def get_retriever():
    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL,
        base_url=OLLAMA_BASE_URL
    )
    
    vectorstore = Chroma(
        persist_directory=CHROMA_DB_DIR,
        embedding_function=embeddings
    )
    
    return vectorstore.as_retriever(search_kwargs={"k": 3})
