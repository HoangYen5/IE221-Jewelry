from ..schemas.categorySchema import CategoryCreate, CategoryUpdate, CategoryResponse
from typing import Dict, Any, List
from fastapi import APIRouter, Depends
from ..service.productService import list_categories
from ..middleware.authMiddleware import verifyToken

router = APIRouter(prefix="/api", tags=["categories"])


@router.get("/categories", status_code=200)
def get_categories(user=Depends(verifyToken)):
    return {"errCode": 0, "data": list_categories()}
