from pydantic import BaseModel
from typing import Optional


class ReportCreate(BaseModel):
    Thang: int
    Nam: int
    MaSanPham: str
    TonDau: Optional[int] = 0
    SoLuongMuaVao: Optional[int] = 0
    SoLuongBanRa: Optional[int] = 0
    TonCuoi: Optional[int] = 0


class ReportResponse(ReportCreate):
    TenSanPham: Optional[str] = None
