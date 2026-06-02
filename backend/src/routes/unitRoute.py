from ..schemas.unitSchema import UnitCreate, UnitUpdate, UnitResponse
from typing import Dict, Any, List
from fastapi import APIRouter, Depends, HTTPException
from ..service import unitService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api/units", tags=["units"]) 

@router.get("/", status_code=200)
def list_units(user=Depends(verifyToken)):
    """Get a list of all units of measurement."""
    return {"errCode": 0, "data": unitService.list_units()}

@router.get("/search", status_code=200)
def search_units(q: str = "", user=Depends(verifyToken)):
    """Search units by keyword."""
    return {"errCode": 0, "data": unitService.search_units(q)}

@router.get("/next-code", status_code=200)
def get_next_code(user=Depends(verifyToken)):
    """Get the next available unit code."""
    code = unitService.get_next_code()
    return {"errCode": 0, "data": code}

@router.get("/{unit_id}", status_code=200)
def get_unit(unit_id: str, user=Depends(verifyToken)):
    """Get a specific unit by ID."""
    u = unitService.get_unit(unit_id)
    if not u:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Unit not found"})
    return {"errCode":0, "data": u}

@router.post("/", status_code=201)
def create_unit(payload: UnitCreate, user=Depends(verifyToken)):
    """Create a new unit of measurement."""
    nid = unitService.create_unit(payload.model_dump())
    return {"errCode":0, "insertId": nid}

@router.put("/{unit_id}", status_code=200)
def update_unit(unit_id: str, payload: UnitUpdate, user=Depends(verifyToken)):
    """Update an existing unit of measurement."""
    affected = unitService.update_unit(unit_id, payload.model_dump(exclude_unset=True))
    if affected == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Unit not found or no change"})
    return {"errCode":0, "affected": affected}

@router.delete("/{unit_id}", status_code=200)
def delete_unit(unit_id: str, user=Depends(verifyToken)):
    """Delete a unit of measurement."""
    removed = unitService.delete_unit(unit_id)
    if removed == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Unit not found"})
    return {"errCode":0, "deleted": removed}
