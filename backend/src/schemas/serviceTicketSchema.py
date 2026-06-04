from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ServiceTicketBase(BaseModel):
    NgayLap: Optional[datetime] = None
    MaKH: str
    TongTien: Optional[float] = 0
    TongTienTraTruoc: Optional[float] = 0
    TongTienConLai: Optional[float] = 0
    TinhTrang: Optional[str] = 'Đang xử lý'

class ServiceTicketDetail(BaseModel):
    MaLoaiDV: str
    DonGiaDuocTinh: float
    SoLuong: int = 1
    ThanhTien: Optional[float] = 0
    TraTruoc: Optional[float] = 0
    ConLai: Optional[float] = 0
    NgayGiao: Optional[datetime] = None
    TinhTrang: Optional[str] = 'Chưa hoàn thành'

class ServiceticketCreate(ServiceTicketBase):
    SoPhieuDV: Optional[str] = None
    details: Optional[List[ServiceTicketDetail]] = None

class ServiceticketUpdate(BaseModel):
    MaKH: Optional[str] = None
    TinhTrang: Optional[str] = None
    TongTien: Optional[float] = None
    TongTienTraTruoc: Optional[float] = None
    TongTienConLai: Optional[float] = None
    details: Optional[List[ServiceTicketDetail]] = None

class ServiceticketStatusUpdate(BaseModel):
    id: str
    status: str

class ServiceticketDelete(BaseModel):
    ids: List[str]

class ServiceticketResponse(ServiceTicketBase):
    SoPhieuDV: str
    details: Optional[List[ServiceTicketDetail]] = None
