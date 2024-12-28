from openai import OpenAI
from typing import Dict, Any

class AIHandler:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        
    async def process_message(self, message: str, context: Dict[str, Any] = None) -> str:
        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful WhatsApp assistant."},
                {"role": "user", "content": message}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
