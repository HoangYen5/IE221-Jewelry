from fastapi import APIRouter, Depends
from ..service import reportService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api/reports", tags=["reports"]) 

@router.get("/", status_code=200)
def get_reports(user=Depends(verifyToken)):
    return {"errCode": 0, "data": reportService.get_report()}
