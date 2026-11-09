import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from config import CHROMA_DB_DIR, OLLAMA_BASE_URL, EMBEDDING_MODEL

def ingest_all_docs():
    docs_dir = os.path.join(os.path.dirname(__file__), "..", "sample_docs")
    loader = DirectoryLoader(docs_dir, glob="*.md", loader_cls=TextLoader)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(documents)
    
    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL,
        base_url=OLLAMA_BASE_URL
    )
    
    Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR
    )
    
if __name__ == "__main__":
    ingest_all_docs()
