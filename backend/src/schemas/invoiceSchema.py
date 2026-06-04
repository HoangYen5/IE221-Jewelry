from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class InvoiceBase(BaseModel):
    NgayLap: Optional[datetime] = None
    MaKH: str
    TongTien: Optional[float] = 0

class InvoiceDetail(BaseModel):
    MaSanPham: str
    SoLuongBan: int
    DonGiaBan: float
    ThanhTien: Optional[float] = 0

class InvoiceCreate(InvoiceBase):
    SoPhieuBH: Optional[str] = None
    details: Optional[List[InvoiceDetail]] = None

class InvoiceUpdate(InvoiceBase):
    MaKH: Optional[str] = None
    details: Optional[List[InvoiceDetail]] = None

class InvoiceDelete(BaseModel):
    ids: List[str]

class InvoiceResponse(InvoiceBase):
    SoPhieuBH: str
    details: Optional[List[InvoiceDetail]] = None
