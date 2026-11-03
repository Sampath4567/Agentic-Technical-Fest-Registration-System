from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import events, registrations, assistant
from contextlib import asynccontextmanager
from rag.ingest_docs import ingest_all_docs
import os

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize RAG on startup
    if not os.path.exists("chroma_db"):
        print("Ingesting sample docs into ChromaDB...")
        try:
            ingest_all_docs()
            print("Ingestion complete.")
        except Exception as e:
            print(f"Warning: RAG initialization failed - {e}")
    yield

app = FastAPI(title="Agentic Fest Registration API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(events.router)
app.include_router(registrations.router)
app.include_router(assistant.router)

@app.get("/")
def read_root():
    return {"message": "Agentic Technical Fest Registration System is running"}
