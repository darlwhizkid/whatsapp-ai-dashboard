from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, String, Integer
from app.core.database import Base
import numpy as np

class KnowledgeBase(Base):
    __tablename__ = "knowledge_base"
    
    id = Column(Integer, primary_key=True)
    content = Column(String)
    embedding = Column(Vector(1536))
    category = Column(String)
    
    @classmethod
    async def search(cls, query_embedding, limit=5):
        return await db.session.query(cls).order_by(
            cls.embedding.cosine_distance(query_embedding)
        ).limit(limit).all()

class KnowledgeService:
    def __init__(self, gemini_client):
        self.gemini = gemini_client
        
    async def get_relevant_knowledge(self, query: str):
        embedding = await self.gemini.generate_embedding(query)
        results = await KnowledgeBase.search(embedding)
        return self.format_context(results)
