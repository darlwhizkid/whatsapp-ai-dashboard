from datetime import datetime, timedelta
from app.models.appointment import Appointment
from app.services.calendar import CalendarService

class AppointmentService:
    def __init__(self):
        self.calendar = CalendarService()
    
    async def get_available_slots(self, service_type: str, date: datetime):
        technicians = await self.get_available_technicians(service_type, date)
        slots = []
        
        for tech in technicians:
            tech_slots = await self.calendar.get_free_slots(
                technician_id=tech.id,
                date=date,
                duration=timedelta(hours=2)
            )
            slots.extend(tech_slots)
            
        return sorted(slots)
    
    async def book_appointment(self, customer_id: str, slot_id: str, service_type: str):
        appointment = Appointment(
            customer_id=customer_id,
            slot_id=slot_id,
            service_type=service_type,
            status="confirmed"
        )
        
        # Book the slot
        await self.calendar.book_slot(slot_id)
        
        # Schedule reminders
        await self.schedule_reminders(appointment)
        
        return appointment
