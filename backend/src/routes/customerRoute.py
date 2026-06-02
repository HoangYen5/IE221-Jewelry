from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Any
from ..service import customerService
from ..middleware.authMiddleware import verifyToken
from ..schemas.customerSchema import CustomerCreate, CustomerUpdate, CustomerResponse

router = APIRouter(prefix="/api/customers", tags=["customers"]) 

@router.get("/", status_code=200, response_model=Dict[str, Any])
def list_customers(user=Depends(verifyToken)):
    """
    Get a list of all customers.
    """
    return {"errCode": 0, "data": customerService.get_customers()}


@router.get("/{customer_id}", status_code=200, response_model=Dict[str, Any])
def get_customer(customer_id: str, user=Depends(verifyToken)):
    """
    Get details of a specific customer by ID.
    """
    c = customerService.get_customer(customer_id)
    if not c:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Customer not found"})
    return {"errCode":0, "data": c}


@router.post("/", status_code=201)
def create_customer(payload: CustomerCreate, user=Depends(verifyToken)):
    """
    Create a new customer.
    """
    nid = customerService.create_customer(payload.model_dump())
    return {"errCode":0, "insertId": nid}


@router.put("/{customer_id}", status_code=200)
def update_customer(customer_id: str, payload: CustomerUpdate, user=Depends(verifyToken)):
    """
    Update an existing customer.
    """
    affected = customerService.update_customer(customer_id, payload.model_dump(exclude_unset=True))
    if affected == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Customer not found or no change"})
    return {"errCode":0, "affected": affected}


@router.delete("/{customer_id}", status_code=200)
def delete_customer(customer_id: str, user=Depends(verifyToken)):
    """
    Delete a customer.
    """
    removed = customerService.delete_customer(customer_id)
    if removed == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Customer not found"})
    return {"errCode":0, "deleted": removed}
