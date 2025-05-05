from fastapi import APIRouter
from pydantic import BaseModel
from db.mongo import save_journal_entry, get_user_journals

router = APIRouter()

class JournalEntry(BaseModel):
    user_id: str
    text: str
    mood: int

@router.post("/journal")
async def create_entry(entry: JournalEntry):
    await save_journal_entry(entry.user_id, entry.text, entry.mood)
    return {"message": "Journal entry saved", "data": entry}

@router.get("/journal/{user_id}")
async def get_journal(user_id: str):
    return await get_user_journals(user_id)
