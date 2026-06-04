from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class ProductTypeBase(BaseModel):
    TenLoaiSanPham: str
    MaDVT: str
    PhanTramLoiNhuan: Optional[float] = 30

class ProductTypeCreate(ProductTypeBase):
    MaLoaiSanPham: Optional[str] = None

class ProductTypeUpdate(BaseModel):
    MaLoaiSanPham: str
    TenLoaiSanPham: Optional[str] = None
    MaDVT: Optional[str] = None
    PhanTramLoiNhuan: Optional[float] = None

class ProductTypeDelete(BaseModel):
    id: Optional[str] = None
    MaLoaiSanPham: Optional[str] = None

class ProductTypeResponse(ProductTypeBase):
    MaLoaiSanPham: str
    createdAt: Optional[datetime] = None
