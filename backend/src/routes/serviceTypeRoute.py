from ..schemas.serviceTypeSchema import ServicetypeCreate, ServicetypeUpdate, ServicetypeDelete, ServicetypeResponse
from typing import Dict, Any, List
from fastapi import APIRouter, Depends, HTTPException
from ..service import serviceTypeService
from ..middleware.authMiddleware import verifyToken, checkPermission

router = APIRouter(prefix="/api/service-types", tags=["service-types"]) 

@router.get("/", status_code=200)
def list_service_types(user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Get a list of all service types."""
    return {"errCode": 0, "data": serviceTypeService.list_service_types()}

@router.post("/create", status_code=201)
def create_service_type(payload: ServicetypeCreate, user=Depends(checkPermission(["admin", "manager"]))):
    """Create a new service type."""
    nid = serviceTypeService.create_service_type(payload.model_dump())
    return {"errCode":0, "insertId": nid}

@router.post("/update", status_code=200)
def update_service_type(payload: ServicetypeUpdate, user=Depends(checkPermission(["admin", "manager"]))):
    """Update an existing service type."""
    type_id = payload.MaLoaiDV
    if not type_id:
        raise HTTPException(status_code=400, detail={"errCode":1, "message":"Thiếu MaLoaiDV"})
    affected = serviceTypeService.update_service_type(type_id, payload.model_dump(exclude_unset=True))
    if affected == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Service type not found or no change"})
    return {"errCode":0, "affected": affected}

@router.post("/delete", status_code=200)
def delete_service_type(payload: ServicetypeDelete, user=Depends(checkPermission(["admin", "manager"]))):
    """Delete a service type by ID."""
    type_id = payload.id or payload.MaLoaiDV
    if not type_id:
        raise HTTPException(status_code=400, detail={"errCode":1, "message":"Thiếu id"})
    deleted = serviceTypeService.delete_service_type(type_id)
    if deleted == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Service type not found"})
    return {"errCode":0, "deleted": deleted}
