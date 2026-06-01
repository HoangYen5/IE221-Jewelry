from fastapi import APIRouter, Depends, HTTPException, status
from ..service import customerService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api/customers", tags=["customers"]) 

@router.get("/", status_code=200)
def list_customers(user=Depends(verifyToken)):
    return {"errCode": 0, "data": customerService.get_customers()}


@router.get("/{customer_id}", status_code=200)
def get_customer(customer_id: str, user=Depends(verifyToken)):
    c = customerService.get_customer(customer_id)
    if not c:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Customer not found"})
    return {"errCode":0, "data": c}


@router.post("/", status_code=201)
def create_customer(payload: dict, user=Depends(verifyToken)):
    nid = customerService.create_customer(payload)
    return {"errCode":0, "insertId": nid}


@router.put("/{customer_id}", status_code=200)
def update_customer(customer_id: str, payload: dict, user=Depends(verifyToken)):
    affected = customerService.update_customer(customer_id, payload)
    if affected == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Customer not found or no change"})
    return {"errCode":0, "affected": affected}


@router.delete("/{customer_id}", status_code=200)
def delete_customer(customer_id: str, user=Depends(verifyToken)):
    removed = customerService.delete_customer(customer_id)
    if removed == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Customer not found"})
    return {"errCode":0, "deleted": removed}
