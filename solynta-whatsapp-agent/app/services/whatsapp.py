from whatsapp_api_client_python import API
from app.models.ticket import Ticket
from app.services.gemini import GeminiAI

class WhatsAppService:
    def __init__(self, config):
        self.api = API(config.WHATSAPP_TOKEN)
        self.ai = GeminiAI()
    
    async def handle_message(self, message: dict):
        customer_id = message['from']
        content = message['text']
        
        # Process with Gemini AI
        response = await self.ai.process_message(content)
        
        if response.requires_escalation:
            ticket = await self.create_ticket(customer_id, content)
            await self.notify_slack(ticket)
        
        await self.send_response(customer_id, response.message)
