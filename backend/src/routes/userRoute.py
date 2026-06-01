from fastapi import APIRouter, HTTPException
from ..service import authService
import jwt, os
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.getenv('JWT_SECRET', 'matkhaucuaban')

router = APIRouter(prefix="/api", tags=["auth"])

@router.post('/login')
def login(payload: dict):
    username = payload.get('TenTaiKhoan') or payload.get('username')
    password = payload.get('MatKhau') or payload.get('password')
    if not username or not password:
        raise HTTPException(status_code=400, detail={'errCode':1, 'message':'Thiếu tài khoản hoặc mật khẩu'})

    user = authService.authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=401, detail={'errCode':1, 'message':'Tên đăng nhập hoặc mật khẩu không đúng'})

    token = jwt.encode(
        {'username': user.get('TenTaiKhoan'), 'Role': user.get('Role')},
        JWT_SECRET,
        algorithm='HS256',
    )

    return {'errCode': 0, 'token': token, 'user': user}

@router.post('/change-password')
def change_password(payload: dict):
    username = payload.get('profilename') or payload.get('TenTaiKhoan') or payload.get('username')
    old_password = payload.get('oldPassword')
    new_password = payload.get('newPassword')

    if not username or not old_password or not new_password:
        raise HTTPException(status_code=400, detail={'errCode':1, 'message':'Thiếu dữ liệu đổi mật khẩu'})

    result = authService.change_password(username, old_password, new_password)
    if not result:
        raise HTTPException(status_code=401, detail={'errCode':2, 'message':'Mật khẩu hiện tại không đúng'})
    return {'errCode': 0, 'message': 'Đổi mật khẩu thành công'}
