from fastapi import FastAPI, Depends, BackgroundTasks
from .core.database import Database
from .core.queue import MessageQueue
from .core.ai_handler import AIHandler
from .core.whatsapp_client import WhatsAppClient
from .config import Settings

app = FastAPI()
settings = Settings()
db = Database(settings)
queue = MessageQueue(settings.REDIS_URL)
ai_handler = AIHandler(settings.OPENAI_API_KEY)
whatsapp_client = WhatsAppClient(settings.WHATSAPP_API_KEY, settings.WHATSAPP_API_URL)

async def process_message(message: str, phone_number: str):
    ai_response = await ai_handler.process_message(message)
    await whatsapp_client.send_message(phone_number, ai_response)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/webhook")
async def handle_message(data: dict, background_tasks: BackgroundTasks):
    message = data.get("message")
    phone_number = data.get("phone")
    
    # Queue message for processing in the background
    background_tasks.add_task(process_message, message, phone_number)
    
    return {"status": "success"}