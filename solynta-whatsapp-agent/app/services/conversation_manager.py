from enum import Enum
from typing import Dict, Any

class ConversationState(Enum):
    INITIAL = "initial"
    COLLECTING_INFO = "collecting_info"
    BOOKING_APPOINTMENT = "booking_appointment"
    CREATING_TICKET = "creating_ticket"
    RESOLVING_ISSUE = "resolving_issue"

class ConversationManager:
    def __init__(self):
        self.states: Dict[str, ConversationState] = {}
        self.context: Dict[str, Dict[str, Any]] = {}
    
    async def process_message(self, customer_id: str, message: str):
        current_state = self.states.get(customer_id, ConversationState.INITIAL)
        context = self.context.get(customer_id, {})
        
        response = await self.handle_state(
            customer_id,
            current_state,
            message,
            context
        )
        
        return response
    
    async def handle_state(self, customer_id: str, state: ConversationState, 
                          message: str, context: Dict):
        if state == ConversationState.INITIAL:
            return await self.handle_initial_state(message)
        elif state == ConversationState.BOOKING_APPOINTMENT:
            return await self.handle_appointment_booking(customer_id, message, context)
        elif state == ConversationState.CREATING_TICKET:
            return await self.handle_ticket_creation(customer_id, message, context)
