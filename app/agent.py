import os
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import asyncio


openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

chat = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.3, model_name="gpt-4")

async def ask_agent(user_input: str) -> str:
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(
        None,
        lambda: chat([HumanMessage(content=user_input)]).content
    )
    return result
