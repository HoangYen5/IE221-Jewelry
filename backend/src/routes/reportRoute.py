from ..schemas.reportSchema import ReportResponse
from fastapi import APIRouter, Depends
from ..service import reportService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api", tags=["reports"]) 

@router.get("/report", status_code=200)
def get_report(month: int = None, year: int = None, user=Depends(verifyToken)):
    """Get inventory report, optionally filtered by month and year."""
    params = {}
    if month is not None:
        params['month'] = month
    if year is not None:
        params['year'] = year
    return {"errCode": 0, "data": reportService.get_report(params if params else None)}
