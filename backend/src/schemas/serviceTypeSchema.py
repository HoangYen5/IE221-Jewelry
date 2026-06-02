from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class ServicetypeBase(BaseModel):
    MaLoaiDV: str
    TenLoaiDV: str
    DonGiaDV: Optional[float] = None
    PhanTramTraTruoc: Optional[float] = None

class ServicetypeCreate(ServicetypeBase):
    pass

class ServicetypeUpdate(ServicetypeBase):
    pass

class ServicetypeResponse(ServicetypeBase):
    pass
