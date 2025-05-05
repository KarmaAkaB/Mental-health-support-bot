from fastapi import FastAPI
from routes.chat import router as chat_router
from routes.journal import router as journal_router

app = FastAPI()

app.include_router(chat_router)
app.include_router(journal_router)
