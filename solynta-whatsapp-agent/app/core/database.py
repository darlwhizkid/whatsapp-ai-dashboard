from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

class Database:
    def __init__(self, config):
        self.engine = create_engine(
            config.DATABASE_URL,
            pool_size=5,
            max_overflow=10,
            pool_timeout=30,
            pool_recycle=1800
        )
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False
        )
        self.Base = declarative_base()
    
    async def get_session(self):
        session = self.SessionLocal()
        try:
            yield session
        finally:
            session.close()
            
    @contextmanager
    def get_sync_session(self):
        session = self.SessionLocal()
        try:
            yield session
        finally:
            session.close()
            
    def create_all(self):
        """Create all database tables"""
        self.Base.metadata.create_all(bind=self.engine)
        
    def drop_all(self):
        """Drop all database tables"""
        self.Base.metadata.drop_all(bind=self.engine)