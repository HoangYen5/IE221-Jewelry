from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class CategoryBase(BaseModel):
    TenLoaiSanPham: str
    MaDVT: str
    PhanTramLoiNhuan: Optional[float] = 30

class CategoryCreate(CategoryBase):
    MaLoaiSanPham: Optional[str] = None

class CategoryUpdate(CategoryBase):
    TenLoaiSanPham: Optional[str] = None
    MaDVT: Optional[str] = None
    PhanTramLoiNhuan: Optional[float] = None

class CategoryResponse(CategoryBase):
    MaLoaiSanPham: str
    createdAt: Optional[datetime] = None
