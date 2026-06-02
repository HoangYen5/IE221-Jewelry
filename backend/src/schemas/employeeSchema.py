from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class EmployeeBase(BaseModel):
    TenTaiKhoan: str
    Role: str
    createdAt: Optional[datetime] = None

class EmployeeCreate(BaseModel):
    TenTaiKhoan: str
    MatKhau: str
    Role: Optional[str] = 'seller'

class EmployeeUpdate(BaseModel):
    TenTaiKhoan: Optional[str] = None
    MatKhau: Optional[str] = None
    Role: Optional[str] = None

class EmployeeResponse(EmployeeBase):
    MaTaiKhoan: int
