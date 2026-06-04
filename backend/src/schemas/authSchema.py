from pydantic import BaseModel
from typing import Optional

class LoginRequest(BaseModel):
    TenTaiKhoan: str
    MatKhau: str

class ChangePasswordRequest(BaseModel):
    TenTaiKhoan: str
    MatKhauCu: str
    MatKhauMoi: str
