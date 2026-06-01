from fastapi import APIRouter, Depends
from ..service import productTypeService
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api/product-types", tags=["product-types"]) 

@router.get("/", status_code=200)
def list_types(user=Depends(verifyToken)):
    return {"errCode": 0, "data": productTypeService.get_types()}
