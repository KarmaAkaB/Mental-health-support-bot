from fastapi import APIRouter
from utils.llm import generate_response
from utils.safety import check_for_crisis
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    if check_for_crisis(request.message):
        return {"response": "I'm here for you. Please consider reaching out to a professional or a helpline."}

    reply = await generate_response(request.message)
    return {"response": reply}
