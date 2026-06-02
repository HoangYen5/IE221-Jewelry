from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class CategoryBase(BaseModel):
    MaLoaiSanPham: str
    TenLoaiSanPham: str
    MaDVT: str
    PhanTramLoiNhuan: Optional[float] = None
    createdAt: Optional[datetime] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    pass
