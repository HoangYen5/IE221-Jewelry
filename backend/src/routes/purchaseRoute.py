from fastapi import APIRouter, Depends, HTTPException
from ..service import purchaseService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api/purchases", tags=["purchases"]) 

@router.get("/", status_code=200)
def list_purchases(user=Depends(verifyToken)):
    return {"errCode": 0, "data": purchaseService.get_purchases()}


@router.get("/{purchase_id}", status_code=200)
def get_purchase(purchase_id: str, user=Depends(verifyToken)):
    p = purchaseService.get_purchase(purchase_id)
    if not p:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Purchase not found"})
    return {"errCode":0, "data": p}


@router.post("/", status_code=201)
def create_purchase(payload: dict, user=Depends(verifyToken)):
    nid = purchaseService.create_purchase(payload)
    return {"errCode":0, "insertId": nid}


@router.put("/{purchase_id}", status_code=200)
def update_purchase(purchase_id: str, payload: dict, user=Depends(verifyToken)):
    affected = purchaseService.update_purchase(purchase_id, payload)
    if affected == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Purchase not found or no change"})
    return {"errCode":0, "affected": affected}


@router.delete("/{purchase_id}", status_code=200)
def delete_purchase(purchase_id: str, user=Depends(verifyToken)):
    removed = purchaseService.delete_purchase(purchase_id)
    if removed == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Purchase not found"})
    return {"errCode":0, "deleted": removed}
