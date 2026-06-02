from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class StatItem(BaseModel):
    label: str
    value: float
    percentageChange: Optional[float] = None

class DashboardStats(BaseModel):
    revenue: StatItem
    customers: StatItem
    orders: StatItem

class DashboardResponse(BaseModel):
    errCode: int
    data: DashboardStats
