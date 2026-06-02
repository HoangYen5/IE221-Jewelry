from ..schemas.dashboardSchema import DashboardResponse, DashboardStats
from typing import Dict, Any, List
from fastapi import APIRouter, Depends
from ..service import dashboardService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"]) 

@router.get("/stats", status_code=200)
def stats(user=Depends(verifyToken)):
    return {"errCode": 0, "data": dashboardService.get_stats()}

@router.get("/revenue", status_code=200)
def revenue(user=Depends(verifyToken)):
    return {"errCode": 0, "data": dashboardService.get_revenue()}

@router.get("/category", status_code=200)
def category(user=Depends(verifyToken)):
    return {"errCode": 0, "data": dashboardService.get_category()}

@router.get("/orders", status_code=200)
def order(user=Depends(verifyToken)):
    return {"errCode": 0, "data": dashboardService.get_order()}