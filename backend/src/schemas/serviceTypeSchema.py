from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class ServiceTypeBase(BaseModel):
    TenLoaiDV: str
    DonGiaDV: Optional[float] = 0
    PhanTramTraTruoc: Optional[float] = 0.5

class ServicetypeCreate(ServiceTypeBase):
    MaLoaiDV: Optional[str] = None

class ServicetypeUpdate(BaseModel):
    MaLoaiDV: str
    TenLoaiDV: Optional[str] = None
    DonGiaDV: Optional[float] = None
    PhanTramTraTruoc: Optional[float] = None

class ServicetypeDelete(BaseModel):
    id: Optional[str] = None
    MaLoaiDV: Optional[str] = None

class ServicetypeResponse(ServiceTypeBase):
    MaLoaiDV: str
    createdAt: Optional[datetime] = None
