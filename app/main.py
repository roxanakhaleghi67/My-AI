from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .agent import ask_agent
from .db import init_db, log_conversation

app = FastAPI(
    title="My AI Assistant",
    description="LangChain + OpenAI based Chat Agent",
    version="1.0.0"
)

init_db()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        reply = await ask_agent(request.message)
        log_conversation(request.message, reply)
        return ChatResponse(reply=reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
