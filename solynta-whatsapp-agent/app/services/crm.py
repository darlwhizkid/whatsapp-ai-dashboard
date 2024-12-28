class CRMService:
    def __init__(self, config):
        self.client = CRMClient(config.CRM_API_KEY)
    
    async def update_customer_interaction(self, customer_id: str, interaction: dict):
        # Record the interaction in CRM
        await self.client.create_interaction(
            customer_id=customer_id,
            channel="whatsapp",
            interaction_type=interaction['type'],
            details=interaction['details']
        )
    
    async def get_customer_history(self, customer_id: str):
        # Fetch customer history from CRM
        return await self.client.get_customer_history(customer_id)
    
    async def update_case(self, ticket: Ticket):
        # Sync ticket updates with CRM
        await self.client.update_case(
            case_id=ticket.crm_case_id,
            status=ticket.status,
            resolution=ticket.resolution
        )
