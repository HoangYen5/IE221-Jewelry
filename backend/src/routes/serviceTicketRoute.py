from ..schemas.serviceTicketSchema import ServiceticketCreate, ServiceticketUpdate, ServiceticketResponse
from typing import Dict, Any, List
from fastapi import APIRouter, Depends, HTTPException
from ..service import serviceTicketService
from ..middleware.authMiddleware import verifyToken, checkPermission

router = APIRouter(prefix="/api/service-tickets", tags=["service-tickets"]) 

@router.get("/", status_code=200)
def list_tickets(user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Get a list of all service tickets."""
    return {"errCode": 0, "data": serviceTicketService.list_tickets()}

@router.get("/{ticket_id}", status_code=200)
def get_ticket(ticket_id: str, user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Get details of a specific service ticket by ID."""
    t = serviceTicketService.get_ticket(ticket_id)
    if not t:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Service ticket not found"})
    return {"errCode":0, "data": t}

@router.post("/create", status_code=201)
def create_ticket(payload: ServiceticketCreate, user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Create a new service ticket with details."""
    nid = serviceTicketService.create_ticket(payload.model_dump())
    return {"errCode":0, "insertId": nid}

@router.post("/status", status_code=200)
def update_ticket_status(payload: dict, user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Update the status of a service ticket."""
    ticket_id = payload.get("id")
    status = payload.get("status")
    if not ticket_id or not status:
        raise HTTPException(status_code=400, detail={"errCode":1, "message":"Thiếu id hoặc status"})
    affected = serviceTicketService.update_ticket_status(ticket_id, status)
    if affected == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Service ticket not found"})
    return {"errCode":0, "affected": affected}

@router.post("/delete", status_code=200)
def delete_tickets(payload: dict, user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Delete one or more service tickets by IDs."""
    ids = payload.get("ids", [])
    if not ids:
        raise HTTPException(status_code=400, detail={"errCode":1, "message":"Thiếu danh sách phiếu dịch vụ"})
    deleted = serviceTicketService.delete_tickets(ids)
    return {"errCode":0, "deleted": deleted}
