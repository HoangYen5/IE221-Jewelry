from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class ProductBase(BaseModel):
    MaSanPham: str
    TenSanPham: str
    MaLoaiSanPham: str
    SoLuongTon: Optional[int] = None
    DonGiaMuaVao: Optional[float] = None
    DonGiaBanRa: Optional[float] = None
    HinhAnh: Optional[str] = None
    MaVach: Optional[str] = None
    isDelete: Optional[bool] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    pass

class ProductActionRequest(BaseModel):
    id: Optional[str] = None
    MaSanPham: Optional[str] = None
    ids: Optional[List[str]] = None
