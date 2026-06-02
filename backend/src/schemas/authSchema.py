from pydantic import BaseModel
from typing import Optional

class LoginRequest(BaseModel):
    TenTaiKhoan: str
    MatKhau: str

class ChangePasswordRequest(BaseModel):
    username: str
    oldPassword: str
    newPassword: str
