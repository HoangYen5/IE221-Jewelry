from ..models import serviceTicketModel

def list_tickets():
    return serviceTicketModel.getAllServiceTickets()
