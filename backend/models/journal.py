from pydantic import BaseModel

class JournalEntry(BaseModel):
    user_id: str
    text: str
    mood: int
