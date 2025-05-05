import openai
from decouple import config

openai.api_key = config("OPENAI_API_KEY")

async def generate_response(user_message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Respond empathetically to: {user_message}",
        max_tokens=150
    )
    return response.choices[0].text.strip()
