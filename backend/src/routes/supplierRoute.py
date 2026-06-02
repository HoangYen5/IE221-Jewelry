from ..schemas.supplierSchema import SupplierCreate, SupplierUpdate, SupplierResponse
from typing import Dict, Any, List
from fastapi import APIRouter, Depends, HTTPException
from ..service import supplierService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api/suppliers", tags=["suppliers"]) 

@router.get("/", status_code=200)
def list_suppliers(user=Depends(verifyToken)):
    return {"errCode": 0, "data": supplierService.list_suppliers()}


@router.get("/{supplier_id}", status_code=200)
def get_supplier(supplier_id: str, user=Depends(verifyToken)):
    s = supplierService.get_supplier(supplier_id)
    if not s:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Supplier not found"})
    return {"errCode":0, "data": s}


@router.post("/", status_code=201)
def create_supplier(payload: SupplierCreate, user=Depends(verifyToken)):
    nid = supplierService.create_supplier(payload.model_dump())
    return {"errCode":0, "insertId": nid}


@router.put("/{supplier_id}", status_code=200)
def update_supplier(supplier_id: str, payload: SupplierUpdate, user=Depends(verifyToken)):
    affected = supplierService.update_supplier(supplier_id, payload.model_dump(exclude_unset=True))
    if affected == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Supplier not found or no change"})
    return {"errCode":0, "affected": affected}


@router.delete("/{supplier_id}", status_code=200)
def delete_supplier(supplier_id: str, user=Depends(verifyToken)):
    removed = supplierService.delete_supplier(supplier_id)
    if removed == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Supplier not found"})
    return {"errCode":0, "deleted": removed}
