from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, List

class Ticket(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    customer_id: str
    issue_type: str
    description: str
    status: str = "open"
    priority: str = "medium"
    created_at: datetime = Field(default_factory=datetime.now)
    assigned_to: Optional[str] = None
    slack_thread_id: Optional[str] = None
    resolution: Optional[str] = None
    
    class Config:
        orm_mode = True
