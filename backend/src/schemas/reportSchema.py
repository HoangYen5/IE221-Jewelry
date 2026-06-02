from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class ReportBase(BaseModel):
    Thang: int
    Nam: int
    MaSanPham: str
    TonDau: Optional[int] = None
    SoLuongMuaVao: Optional[int] = None
    SoLuongBanRa: Optional[int] = None
    TonCuoi: Optional[int] = None

class ReportCreate(ReportBase):
    pass

class ReportUpdate(ReportBase):
    pass

class ReportResponse(ReportBase):
    pass
