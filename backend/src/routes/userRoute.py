from fastapi import APIRouter, HTTPException, Depends
from ..service import authService
from ..schemas.authSchema import LoginRequest, ChangePasswordRequest
from ..middleware.authMiddleware import verifyToken
import jwt, os
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET = os.getenv('JWT_SECRET', 'matkhaucuaban')

router = APIRouter(prefix="/api", tags=["auth"])

@router.post('/login')
def login(payload: LoginRequest):
    """
    Authenticate a user and return a JWT token.
    """
    username = payload.TenTaiKhoan
    password = payload.MatKhau
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
def change_password(payload: ChangePasswordRequest, user=Depends(verifyToken)):
    """
    Change user password.
    """
    username = payload.TenTaiKhoan
    old_password = payload.MatKhauCu
    new_password = payload.MatKhauMoi

    if not username or not old_password or not new_password:
        raise HTTPException(status_code=400, detail={'errCode':1, 'message':'Thiếu dữ liệu đổi mật khẩu'})

    result = authService.change_password(username, old_password, new_password)
    if not result:
        raise HTTPException(status_code=401, detail={'errCode':2, 'message':'Mật khẩu hiện tại không đúng'})
    return {'errCode': 0, 'message': 'Đổi mật khẩu thành công'}
