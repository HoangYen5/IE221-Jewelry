from fastapi import APIRouter, Depends
from ..service import dashboardService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"]) 

@router.get("/", status_code=200)
def stats(user=Depends(verifyToken)):
    return {"errCode": 0, "data": dashboardService.get_stats()}
