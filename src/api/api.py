from fastapi import FastAPI
from src.retrieval.retriever import retrieve, locate_files
from src.llm.prompt import ask_llm
from pydantic import BaseModel
from src.bootstrap import bootstrap
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    bootstrap()
    yield

app = FastAPI(
    title="Code Search RAG",
    lifespan=lifespan
)

class AskRequest(BaseModel):
    query: str

@app.post("/ask-about-design")
def ask(ask: AskRequest):
    ctx = retrieve(ask.query, 2)
    return ask_llm(ask.query, ctx)

@app.post("/file-locator")
def file_locator(ask: AskRequest):
    files = locate_files(ask.query, 5)
    return {
        "query": ask.query,
        "files": files
    }