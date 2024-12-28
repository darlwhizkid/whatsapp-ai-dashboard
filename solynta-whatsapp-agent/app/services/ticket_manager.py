from app.models.ticket import Ticket
from app.services.slack import SlackService
from app.services.crm import CRMService

class TicketManager:
    def __init__(self):
        self.slack = SlackService()
        self.crm = CRMService()
    
    async def create_ticket(self, customer_id: str, issue: str, priority: str):
        # Create ticket
        ticket = Ticket(
            customer_id=customer_id,
            description=issue,
            priority=priority
        )
        
        # Update CRM
        await self.crm.create_case(ticket)
        
        # Notify Slack
        slack_thread = await self.slack.notify_ticket(ticket)
        ticket.slack_thread_id = slack_thread
        
        # Set SLA timer
        await self.set_sla_timer(ticket)
        
        return ticket
    
    async def update_ticket(self, ticket_id: str, update: dict):
        ticket = await Ticket.get(ticket_id)
        
        # Update ticket status
        ticket.update(update)
        
        # Sync with CRM
        await self.crm.update_case(ticket)
        
        # Notify customer via WhatsApp
        await self.notify_customer(ticket)
        
        # Update Slack thread
        await self.slack.update_thread(ticket)
