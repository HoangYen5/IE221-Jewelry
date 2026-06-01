from fastapi import APIRouter, Depends
from ..service import serviceTicketService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api/service-tickets", tags=["service-tickets"]) 

@router.get("/", status_code=200)
def list_tickets(user=Depends(verifyToken)):
    return {"errCode": 0, "data": serviceTicketService.list_tickets()}
