from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackService:
    def __init__(self, config):
        self.client = WebClient(token=config.SLACK_TOKEN)
        self.channel = config.SLACK_CHANNEL
    
    async def notify_ticket(self, ticket: Ticket):
        try:
            response = await self.client.chat_postMessage(
                channel=self.channel,
                text=f"New Support Ticket: {ticket.id}\n"
                     f"Customer: {ticket.customer_id}\n"
                     f"Issue: {ticket.description}"
            )
            return response['ts']  # Thread ID for future updates
        except SlackApiError as e:
            logger.error(f"Slack notification failed: {e}")
