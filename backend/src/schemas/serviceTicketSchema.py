from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ServiceticketBase(BaseModel):
    SoPhieuDV: Optional[str] = None
    NgayLap: Optional[datetime] = None
    MaKH: str
    TongTien: Optional[float] = None
    TongTienTraTruoc: Optional[float] = None
    TongTienConLai: Optional[float] = None
    TinhTrang: Optional[str] = None

class ServiceticketDetail(BaseModel):
    MaLoaiDV: str
    DonGiaDuocTinh: float
    SoLuong: int
    ThanhTien: Optional[float] = None
    TraTruoc: Optional[float] = None
    ConLai: Optional[float] = None
    NgayGiao: Optional[datetime] = None
    TinhTrang: Optional[str] = None

class ServiceticketCreate(ServiceticketBase):
    details: Optional[List[ServiceticketDetail]] = None

class ServiceticketUpdate(ServiceticketBase):
    details: Optional[List[ServiceticketDetail]] = None

class ServiceticketResponse(ServiceticketBase):
    pass
