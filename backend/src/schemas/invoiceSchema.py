from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class InvoiceBase(BaseModel):
    SoPhieuBH: Optional[str] = None
    NgayLap: Optional[datetime] = None
    MaKH: str
    TongTien: Optional[float] = None

class InvoiceDetail(BaseModel):
    MaSanPham: str
    SoLuongBan: int
    DonGiaBan: float
    ThanhTien: Optional[float] = None

class InvoiceCreate(InvoiceBase):
    details: Optional[List[InvoiceDetail]] = None

class InvoiceUpdate(InvoiceBase):
    details: Optional[List[InvoiceDetail]] = None

class InvoiceResponse(InvoiceBase):
    pass
