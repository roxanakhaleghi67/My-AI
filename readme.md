# my-AI-assistant

## English

A minimal LangChain + FastAPI + Docker project that exposes a REST API to chat with an OpenAI LLM (GPT-4). All conversations are logged in a SQLite database.

### Features
- FastAPI REST endpoint
- LangChain Agent integration
- OpenAI GPT-4 backend
- Conversation logging to SQLite
- Docker-ready

### Usage
1. Add your OpenAI API key in `.env` file.
2. Build and run with Docker Compose:

docker-compose up --build

3. Access API at:

http://localhost:8000/docs


---

## فارسی

FastAPI + LangChain + Docker

### ویژگی‌ها
- Endpoint رست برای چت
- ایجنت LangChain با OpenAI
- ثبت مکالمات در پایگاه داده SQLite
- آماده اجرا با Docker

### روش اجرا
1. کلون کنید و در پوشه پروژه `.env` بسازید:
OPENAI_API_KEY=کلید خودتان
2. اجرا با داکر کامپوز:
docker-compose up --build
3. مستندات و تست API:
http://localhost:8000/docs


---

## License
MIT

