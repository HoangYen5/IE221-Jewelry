from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class ProductBase(BaseModel):
    TenSanPham: str
    MaLoaiSanPham: str
    SoLuongTon: Optional[int] = 0
    DonGiaMuaVao: Optional[float] = 0
    DonGiaBanRa: Optional[float] = 0
    HinhAnh: Optional[str] = None
    MaVach: Optional[str] = None
    isDelete: Optional[bool] = False

class ProductCreate(ProductBase):
    MaSanPham: Optional[str] = None

class ProductUpdate(ProductBase):
    TenSanPham: Optional[str] = None
    MaLoaiSanPham: Optional[str] = None
    SoLuongTon: Optional[int] = None
    DonGiaMuaVao: Optional[float] = None
    DonGiaBanRa: Optional[float] = None
    HinhAnh: Optional[str] = None
    MaVach: Optional[str] = None
    isDelete: Optional[bool] = None

class ProductResponse(ProductBase):
    MaSanPham: str
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class ProductActionRequest(BaseModel):
    id: Optional[str] = None
    MaSanPham: Optional[str] = None
    ids: Optional[List[str]] = None
