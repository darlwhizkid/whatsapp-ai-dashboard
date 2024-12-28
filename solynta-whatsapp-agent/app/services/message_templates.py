from enum import Enum

class MessageTemplate(Enum):
    WELCOME = """
    Welcome to Solynta Energy! 👋
    I'm your AI assistant here to help with:
    1. Technical Support
    2. Appointments
    3. Billing Inquiries
    4. System Status
    
    Please type a number or describe your need.
    """
    
    APPOINTMENT_PROMPT = """
    Let's schedule your appointment 📅
    Available services:
    1. System Maintenance
    2. Technical Inspection
    3. New Installation
    4. Repairs
    
    Please select a service type:
    """
    
    TICKET_CREATED = """
    Ticket #{ticket_id} has been created.
    Priority: {priority}
    Our team will respond within:
    High: 2 hours
    Medium: 4 hours
    Low: 24 hours
    
    You'll receive updates here on WhatsApp.
    """
