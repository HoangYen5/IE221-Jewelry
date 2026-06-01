from fastapi import APIRouter, Depends, HTTPException
from ..service import employeeService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api/employees", tags=["employees"]) 

@router.get("/", status_code=200)
def list_employees(user=Depends(verifyToken)):
    return {"errCode": 0, "data": employeeService.get_employees()}


@router.get("/{employee_id}", status_code=200)
def get_employee(employee_id: str, user=Depends(verifyToken)):
    e = employeeService.get_employee(employee_id)
    if not e:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Employee not found"})
    return {"errCode":0, "data": e}


@router.post("/", status_code=201)
def create_employee(payload: dict, user=Depends(verifyToken)):
    nid = employeeService.create_employee(payload)
    return {"errCode":0, "insertId": nid}


@router.put("/{employee_id}", status_code=200)
def update_employee(employee_id: str, payload: dict, user=Depends(verifyToken)):
    affected = employeeService.update_employee(employee_id, payload)
    if affected == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Employee not found or no change"})
    return {"errCode":0, "affected": affected}


@router.delete("/{employee_id}", status_code=200)
def delete_employee(employee_id: str, user=Depends(verifyToken)):
    removed = employeeService.delete_employee(employee_id)
    if removed == 0:
        raise HTTPException(status_code=404, detail={"errCode":4, "message":"Employee not found"})
    return {"errCode":0, "deleted": removed}
