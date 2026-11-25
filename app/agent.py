"""Conversation agent backed by an OpenAI chat model and LangChain memory.

The chat model is created lazily on the first model call, so importing this
module never requires ``OPENAI_API_KEY`` and never performs network access.
"""

import asyncio
import os
from typing import Dict

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOpenAI

DEFAULT_SESSION_ID = "default"
MODEL_NAME = "gpt-4"
TEMPERATURE = 0.3

_llm = None
_chains: Dict[str, ConversationChain] = {}


def _get_llm() -> ChatOpenAI:
    """Create the chat model on first use and require the API key then."""
    global _llm
    if _llm is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "OPENAI_API_KEY is not set. Provide it in the environment "
                "or in a .env file before calling the model."
            )
        _llm = ChatOpenAI(
            openai_api_key=api_key,
            temperature=TEMPERATURE,
            model_name=MODEL_NAME,
        )
    return _llm


def _get_chain(session_id: str) -> ConversationChain:
    """Return the chain for a session, keeping its conversation memory."""
    chain = _chains.get(session_id)
    if chain is None:
        chain = ConversationChain(
            llm=_get_llm(),
            memory=ConversationBufferMemory(),
            verbose=False,
        )
        _chains[session_id] = chain
    return chain


async def ask_agent(user_input: str, session_id: str = DEFAULT_SESSION_ID) -> str:
    """Send a message to the model with the session's conversation memory."""
    chain = _get_chain(session_id)
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, lambda: chain.predict(input=user_input))
