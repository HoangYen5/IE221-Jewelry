from ..schemas.profileSchema import ProfileResponse
from fastapi import APIRouter, Depends
from ..service import profileService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api", tags=["profile"])


@router.get("/profile")
def get_profile(user=Depends(verifyToken)):
    """Get current user profile from JWT token."""
    username = user.get('username') if isinstance(user, dict) else None
    return {"errCode": 0, "data": profileService.get_profile(username)}


@router.get("/get-all-profiles")
def get_all_profiles(user=Depends(verifyToken)):
    """Get current user profile (alias for frontend compatibility)."""
    username = user.get('username') if isinstance(user, dict) else None
    return {"errCode": 0, "data": profileService.get_profile(username)}
