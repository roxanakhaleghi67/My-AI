from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./conversations.db"

Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True, index=True)
    user_input = Column(String, nullable=False)
    agent_reply = Column(String, nullable=False)

def init_db():
    Base.metadata.create_all(bind=engine)

def log_conversation(user_input: str, agent_reply: str):
    session = SessionLocal()
    conversation = Conversation(user_input=user_input, agent_reply=agent_reply)
    session.add(conversation)
    session.commit()
    session.close()
