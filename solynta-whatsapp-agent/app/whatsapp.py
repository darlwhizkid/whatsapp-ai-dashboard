from fastapi import FastAPI, WebSocket, Depends
from sqlalchemy.orm import Session
from .core.database import Database
from .crud import WhatsAppCRUD
from .websocket import ConnectionManager

app = FastAPI()
manager = ConnectionManager()

@app.post("/webhook")
async def whatsapp_webhook(data: dict, db: Session = Depends(Database.get_session)):
    # Handle incoming WhatsApp messages
    message = data.get("message")
    phone_number = data.get("phone")
    
    # Save message to database
    user = WhatsAppCRUD.create_user(db, phone_number, "Unknown")
    chat = WhatsAppCRUD.save_message(db, user.id, message)
    
    # Process with AI and save response
    ai_response = "AI Response here"  # Replace with actual AI integration
    ai_chat = WhatsAppCRUD.save_message(db, user.id, ai_response, is_ai_response=True)
    
    return {"status": "success"}

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client {client_id}: {data}")
    except:
        await manager.disconnect(websocket)
