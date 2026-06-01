from fastapi import APIRouter, Depends
from ..service import invoiceService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api/invoices", tags=["invoices"]) 

@router.get("/", status_code=200)
def list_invoices(user=Depends(verifyToken)):
    return {"errCode": 0, "data": invoiceService.get_invoices()}
    
@router.get("/{invoice_id}", status_code=200)
def get_invoice(invoice_id: str, user=Depends(verifyToken)):
    inv = invoiceService.get_invoice(invoice_id)
    if not inv:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Invoice not found"})
    return {"errCode":0, "data": inv}

@router.post("/", status_code=201)
def create_invoice(payload: dict, user=Depends(verifyToken)):
    nid = invoiceService.create_invoice(payload)
    return {"errCode":0, "insertId": nid}

@router.put("/{invoice_id}", status_code=200)
def update_invoice(invoice_id: str, payload: dict, user=Depends(verifyToken)):
    affected = invoiceService.update_invoice(invoice_id, payload)
    if affected == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Invoice not found or no change"})
    return {"errCode":0, "affected": affected}

@router.delete("/{invoice_id}", status_code=200)
def delete_invoice(invoice_id: str, user=Depends(verifyToken)):
    removed = invoiceService.delete_invoice(invoice_id)
    if removed == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Invoice not found"})
    return {"errCode":0, "deleted": removed}
