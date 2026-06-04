from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class CustomerBase(BaseModel):
    TenKH: str
    SoDienThoai: Optional[str] = None
    DiaChi: Optional[str] = None

class CustomerCreate(CustomerBase):
    MaKH: Optional[str] = None

class CustomerUpdate(CustomerBase):
    TenKH: Optional[str] = None

class CustomerResponse(CustomerBase):
    MaKH: str
    createdAt: Optional[datetime] = None
