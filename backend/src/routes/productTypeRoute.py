from ..schemas.productTypeSchema import ProducttypeCreate, ProducttypeUpdate, ProducttypeResponse
from typing import Dict, Any, List
from fastapi import APIRouter, Depends, HTTPException
from ..service import productTypeService
from ..middleware.authMiddleware import verifyToken, checkPermission

router = APIRouter(prefix="/api/product-types", tags=["product-types"]) 

@router.get("/", status_code=200)
def list_types(user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Get a list of all product types (categories)."""
    return {"errCode": 0, "data": productTypeService.get_types()}

@router.post("/create", status_code=201)
def create_type(payload: ProducttypeCreate, user=Depends(checkPermission(["admin", "manager"]))):
    """Create a new product type."""
    nid = productTypeService.create_type(payload.model_dump())
    return {"errCode":0, "insertId": nid}

@router.post("/update", status_code=200)
def update_type(payload: ProducttypeUpdate, user=Depends(checkPermission(["admin", "manager"]))):
    """Update an existing product type."""
    type_id = payload.MaLoaiSanPham
    if not type_id:
        raise HTTPException(status_code=400, detail={"errCode":1, "message":"Thiếu MaLoaiSanPham"})
    affected = productTypeService.update_type(type_id, payload.model_dump(exclude_unset=True))
    if affected == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Product type not found or no change"})
    return {"errCode":0, "affected": affected}

@router.post("/delete", status_code=200)
def delete_type(payload: dict, user=Depends(checkPermission(["admin", "manager"]))):
    """Delete a product type by ID."""
    type_id = payload.get("id") or payload.get("MaLoaiSanPham")
    if not type_id:
        raise HTTPException(status_code=400, detail={"errCode":1, "message":"Thiếu id"})
    deleted = productTypeService.delete_type(type_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Product type not found"})
    return {"errCode":0, "deleted": deleted}
