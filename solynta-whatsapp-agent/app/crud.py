from sqlalchemy.orm import Session
from . import models

class WhatsAppCRUD:
    @staticmethod
    def create_user(db: Session, phone_number: str, name: str):
        user = models.User(phone_number=phone_number, name=name)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def save_message(db: Session, user_id: int, message: str, is_ai_response: bool = False):
        chat = models.Chat(user_id=user_id, message=message, is_ai_response=is_ai_response)
        db.add(chat)
        db.commit()
        db.refresh(chat)
        return chat
