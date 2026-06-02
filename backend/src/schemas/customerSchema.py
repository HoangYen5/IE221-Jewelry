from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class CustomerBase(BaseModel):
    MaKH: str
    TenKH: str
    SoDienThoai: Optional[str] = None
    DiaChi: Optional[str] = None
    createdAt: Optional[datetime] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    pass
