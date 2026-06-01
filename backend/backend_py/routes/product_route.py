from fastapi import APIRouter, Depends, HTTPException
from ..models import product_model
from ..middleware.auth_middleware import verify_token

router = APIRouter(prefix="/api/products", tags=["products"]) 

@router.get("")
def list_products(user=Depends(verify_token)):
    try:
        rows = product_model.get_all_products()
        return {"errCode": 0, "data": rows}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("")
def create_product(payload: dict, user=Depends(verify_token)):
    try:
        new_id = product_model.create_product(payload)
        return {"errCode": 0, "insertId": new_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("")
def update_product(payload: dict, user=Depends(verify_token)):
    try:
        updated = product_model.update_product(payload)
        return {"errCode": 0, "affected": updated}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
