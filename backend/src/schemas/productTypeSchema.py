from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class ProducttypeBase(BaseModel):
    MaLoaiSanPham: str
    TenLoaiSanPham: str
    MaDVT: str
    PhanTramLoiNhuan: Optional[float] = None
    createdAt: Optional[datetime] = None

class ProducttypeCreate(ProducttypeBase):
    pass

class ProducttypeUpdate(ProducttypeBase):
    pass

class ProducttypeResponse(ProducttypeBase):
    pass
