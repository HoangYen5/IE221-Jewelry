from ..schemas.invoiceSchema import InvoiceCreate, InvoiceUpdate, InvoiceResponse
from typing import Dict, Any, List
from fastapi import APIRouter, Depends, HTTPException
from ..service import invoiceService
from ..middleware.authMiddleware import verifyToken, checkPermission

router = APIRouter(prefix="/api/invoices", tags=["invoices"]) 

@router.get("/", status_code=200)
def list_invoices(user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Get a list of all invoices (sales orders)."""
    return {"errCode": 0, "data": invoiceService.get_invoices()}
    
@router.get("/{invoice_id}", status_code=200)
def get_invoice(invoice_id: str, user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Get details of a specific invoice by ID."""
    inv = invoiceService.get_invoice(invoice_id)
    if not inv:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Invoice not found"})
    return {"errCode":0, "data": inv}

@router.post("/create", status_code=201)
def create_invoice(payload: InvoiceCreate, user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Create a new invoice (sales order) with details."""
    nid = invoiceService.create_invoice(payload.model_dump())
    return {"errCode":0, "insertId": nid}

@router.post("/delete", status_code=200)
def delete_invoices(payload: dict, user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Delete one or more invoices by IDs."""
    ids = payload.get("ids", [])
    if not ids:
        raise HTTPException(status_code=400, detail={"errCode":1, "message":"Thiếu danh sách phiếu bán hàng"})
    deleted = invoiceService.delete_invoices(ids)
    return {"errCode":0, "deleted": deleted}
