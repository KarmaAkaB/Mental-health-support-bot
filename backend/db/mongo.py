from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

client = AsyncIOMotorClient(config("MONGO_URI"))
db = client.mh_bot_db

journals = db.journals  # Collection

async def save_journal_entry(user_id, text, mood_score):
    await journals.insert_one({
        "user_id": user_id,
        "entry": text,
        "mood": mood_score,
        "timestamp": datetime.utcnow()
    })

async def get_user_journals(user_id):
    return await journals.find({"user_id": user_id}).to_list(100)
