from ..schemas.purchaseSchema import PurchaseCreate, PurchaseUpdate, PurchaseDelete, PurchaseResponse
from typing import Dict, Any, List
from fastapi import APIRouter, Depends, HTTPException
from ..service import purchaseService
from ..middleware.authMiddleware import verifyToken, checkPermission

router = APIRouter(prefix="/api/purchases", tags=["purchases"]) 

@router.get("/", status_code=200)
def list_purchases(user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Get a list of all purchase orders."""
    return {"errCode": 0, "data": purchaseService.get_purchases()}


@router.get("/{purchase_id}", status_code=200)
def get_purchase(purchase_id: str, user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Get details of a specific purchase order by ID."""
    p = purchaseService.get_purchase(purchase_id)
    if not p:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Purchase not found"})
    return {"errCode":0, "data": p}


@router.post("/create", status_code=201)
def create_purchase(payload: PurchaseCreate, user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Create a new purchase order with details."""
    nid = purchaseService.create_purchase(payload.model_dump())
    return {"errCode":0, "insertId": nid}


@router.post("/delete", status_code=200)
def delete_purchases(payload: PurchaseDelete, user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Delete one or more purchase orders by IDs."""
    ids = payload.ids
    if not ids:
        raise HTTPException(status_code=400, detail={"errCode":1, "message":"Thiếu danh sách phiếu mua hàng"})
    deleted = purchaseService.delete_purchases(ids)
    return {"errCode":0, "deleted": deleted}
