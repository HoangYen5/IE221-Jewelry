from fastapi import APIRouter, Depends
from ..service import profileService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api/profile", tags=["profile"]) 

@router.get("")
def get_profile(user=Depends(verifyToken)):
    user_id = user.get('id') if isinstance(user, dict) else None
    return {"errCode": 0, "data": profileService.get_profile(user_id)}
