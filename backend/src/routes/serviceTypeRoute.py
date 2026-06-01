from fastapi import APIRouter, Depends
from ..service import serviceTypeService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api/service-types", tags=["service-types"]) 

@router.get("/", status_code=200)
def list_service_types(user=Depends(verifyToken)):
    return {"errCode": 0, "data": serviceTypeService.list_service_types()}
