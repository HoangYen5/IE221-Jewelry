from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class SupplierBase(BaseModel):
    TenNCC: str
    DiaChi: Optional[str] = None
    SoDienThoai: Optional[str] = None

class SupplierCreate(SupplierBase):
    MaNCC: Optional[str] = None

class SupplierUpdate(SupplierBase):
    TenNCC: Optional[str] = None

class SupplierResponse(SupplierBase):
    MaNCC: str
    createdAt: Optional[datetime] = None
