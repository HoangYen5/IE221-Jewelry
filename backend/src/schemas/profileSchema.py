from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProfileResponse(BaseModel):
    MaTaiKhoan: Optional[int] = None
    TenTaiKhoan: Optional[str] = None
    Role: Optional[str] = None
    createdAt: Optional[datetime] = None
