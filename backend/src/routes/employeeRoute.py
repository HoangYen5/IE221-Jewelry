from ..schemas.employeeSchema import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from typing import Dict, Any, List
from fastapi import APIRouter, Depends, HTTPException
from ..service import employeeService
from ..middleware.authMiddleware import verifyToken, checkPermission

router = APIRouter(prefix="/api/employees", tags=["employees"]) 

@router.get("/", status_code=200)
def list_employees(user=Depends(checkPermission(["admin"]))):
    return {"errCode": 0, "data": employeeService.get_employees()}


@router.get("/{employee_id}", status_code=200)
def get_employee(employee_id: str, user=Depends(checkPermission(["admin"]))):
    e = employeeService.get_employee(employee_id)
    if not e:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Employee not found"})
    return {"errCode":0, "data": e}


@router.post("/", status_code=201)
def create_employee(payload: EmployeeCreate, user=Depends(checkPermission(["admin"]))):
    nid = employeeService.create_employee(payload.model_dump())
    return {"errCode":0, "insertId": nid}


@router.put("/{employee_id}", status_code=200)
def update_employee(employee_id: str, payload: EmployeeUpdate, user=Depends(checkPermission(["admin"]))):
    affected = employeeService.update_employee(employee_id, payload.model_dump(exclude_unset=True))
    if affected == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Employee not found or no change"})
    return {"errCode":0, "affected": affected}


@router.delete("/{employee_id}", status_code=200)
def delete_employee(employee_id: str, user=Depends(checkPermission(["admin"]))):
    removed = employeeService.delete_employee(employee_id)
    if removed == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Employee not found"})
    return {"errCode":0, "deleted": removed}
