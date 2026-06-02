from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class SupplierBase(BaseModel):
    MaNCC: str
    TenNCC: str
    DiaChi: Optional[str] = None
    SoDienThoai: Optional[str] = None
    createdAt: Optional[datetime] = None

class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(SupplierBase):
    pass

class SupplierResponse(SupplierBase):
    pass
