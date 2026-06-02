from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class UnitBase(BaseModel):
    MaDVT: str
    TenDVT: str
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class UnitCreate(UnitBase):
    pass

class UnitUpdate(UnitBase):
    pass

class UnitResponse(UnitBase):
    pass
