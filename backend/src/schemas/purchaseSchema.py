from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PurchaseBase(BaseModel):
    NgayLap: Optional[datetime] = None
    MaNCC: str
    TongTien: Optional[float] = 0

class PurchaseDetail(BaseModel):
    MaSanPham: str
    SoLuongMua: int
    DonGiaMua: float
    ThanhTien: Optional[float] = 0

class PurchaseCreate(PurchaseBase):
    SoPhieuMH: Optional[str] = None
    details: Optional[List[PurchaseDetail]] = None

class PurchaseUpdate(PurchaseBase):
    MaNCC: Optional[str] = None
    details: Optional[List[PurchaseDetail]] = None

class PurchaseDelete(BaseModel):
    ids: List[str]

class PurchaseResponse(PurchaseBase):
    SoPhieuMH: str
    details: Optional[List[PurchaseDetail]] = None
