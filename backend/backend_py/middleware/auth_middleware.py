from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

security = HTTPBearer()

JWT_SECRET = os.getenv("JWT_SECRET", "matkhaucuaban")

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=403, detail={"errCode": 2, "message": "Token không hợp lệ hoặc đã hết hạn"})
    except Exception:
        raise HTTPException(status_code=401, detail={"errCode": 1, "message": "Xác thực thất bại"})

def check_permission(allowed_roles: list):
    def checker(user=Depends(verify_token)):
        role = user.get("Role")
        if role in allowed_roles:
            return user
        raise HTTPException(status_code=403, detail={"errCode": 3, "message": f"Bạn không có quyền thực hiện chức năng này. (Role của bạn là: {role})"})
    return checker
