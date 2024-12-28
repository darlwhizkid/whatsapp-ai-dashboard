import httpx
from typing import Dict, Any

class WhatsAppClient:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    async def send_message(self, phone_number: str, message: str):
        async with httpx.AsyncClient() as client:
            payload = {
                "messaging_product": "whatsapp",
                "to": phone_number,
                "type": "text",
                "text": {"body": message}
            }
            response = await client.post(
                f"{self.base_url}/messages",
                headers=self.headers,
                json=payload
            )
            return response.json()
