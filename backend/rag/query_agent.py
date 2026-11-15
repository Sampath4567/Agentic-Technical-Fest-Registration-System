import os
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from rag.retriever import get_retriever
from config import OLLAMA_BASE_URL, OLLAMA_MODEL

def ask_question(question: str):
    retriever = get_retriever()
    retrieved_docs = retriever.invoke(question)
    
    sources = [{"title": os.path.basename(doc.metadata.get("source", "unknown")), "snippet": doc.page_content[:100] + "..."} for doc in retrieved_docs]
    
    if not retrieved_docs:
        return "The available event documents do not contain enough information to answer this question.", []
    
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    
    template = """You are an assistant for a technical fest registration system.
Use the following pieces of retrieved context to answer the question.
If the answer is not in the context, say "The available event documents do not contain enough information to answer this question."
Do not invent information.

Context:
{context}

Question:
{question}

Answer:
"""
    
    prompt = PromptTemplate.from_template(template)
    llm = ChatOllama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL, temperature=0.1)
    
    chain = (
        {"context": lambda x: context, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    answer = chain.invoke(question)
    
    # Verify if hallucinated
    if "do not contain enough information" in answer.lower():
        sources = []
        
    return answer, sources
