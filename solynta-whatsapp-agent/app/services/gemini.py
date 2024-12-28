import google.generativeai as genai
from typing import Dict

class GeminiAI:
    def __init__(self, config):
        genai.configure(api_key=config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        
    async def process_message(self, content: str) -> Dict:
        chat = self.model.start_chat(history=[])
        response = chat.send_message(content)
        
        return {
            'message': response.text,
            'requires_escalation': self._check_escalation_needed(response),
            'sentiment': self._analyze_sentiment(response)
        }
