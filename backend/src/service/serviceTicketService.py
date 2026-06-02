from ..models import serviceTicketModel

def list_tickets():
    return serviceTicketModel.getAllServiceTickets()

def get_ticket(ticket_id):
    return serviceTicketModel.getServiceTicketById(ticket_id)

def create_ticket(data: dict):
    return serviceTicketModel.createServiceTicket(data)

def update_ticket_status(ticket_id, status):
    return serviceTicketModel.updateServiceTicketStatus(ticket_id, status)

def delete_tickets(ticket_ids):
    return serviceTicketModel.deleteServiceTickets(ticket_ids)
