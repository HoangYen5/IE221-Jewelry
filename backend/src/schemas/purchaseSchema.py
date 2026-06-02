from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PurchaseBase(BaseModel):
    SoPhieuMH: Optional[str] = None
    NgayLap: Optional[datetime] = None
    MaNCC: str
    TongTien: Optional[float] = None

class PurchaseDetail(BaseModel):
    MaSanPham: str
    SoLuongMua: int
    DonGiaMua: float
    ThanhTien: Optional[float] = None

class PurchaseCreate(PurchaseBase):
    details: Optional[List[PurchaseDetail]] = None

class PurchaseUpdate(PurchaseBase):
    details: Optional[List[PurchaseDetail]] = None

class PurchaseResponse(PurchaseBase):
    pass
