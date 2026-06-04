from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class UnitBase(BaseModel):
    TenDVT: str

class UnitCreate(UnitBase):
    MaDVT: Optional[str] = None

class UnitUpdate(UnitBase):
    TenDVT: Optional[str] = None

class UnitResponse(UnitBase):
    MaDVT: str
    createdAt: Optional[datetime] = None
