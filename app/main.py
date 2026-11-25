"""FastAPI application: chat endpoint, health check and conversation logging."""

try:
    from dotenv import load_dotenv
except ImportError:  # python-dotenv is optional at runtime
    load_dotenv = None

if load_dotenv is not None:
    load_dotenv()

from fastapi import FastAPI, HTTPException

from .agent import ask_agent
from .db import init_db, log_conversation
from .schemas import ChatRequest, ChatResponse

app = FastAPI(
    title="My AI Assistant",
    description="LangChain + OpenAI based Chat Agent",
    version="1.0.0",
)

init_db()


@app.get("/health")
async def health() -> dict:
    """Liveness probe that does not touch the model or the database."""
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest) -> ChatResponse:
    try:
        reply = await ask_agent(request.message, request.session_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    log_conversation(request.message, reply)
    return ChatResponse(reply=reply)
