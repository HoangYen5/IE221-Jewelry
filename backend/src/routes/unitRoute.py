from fastapi import APIRouter, Depends
from ..service import unitService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api/units", tags=["units"]) 

@router.get("/", status_code=200)
def list_units(user=Depends(verifyToken)):
    return {"errCode": 0, "data": unitService.list_units()}
