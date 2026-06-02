import os
from uuid import uuid4
from fastapi import APIRouter, Depends, HTTPException, Request, UploadFile
from ..service import productService
from ..middleware.authMiddleware import verifyToken
from ..schemas.productSchema import ProductActionRequest

router = APIRouter(prefix="/api/products", tags=["products"]) 


def _save_upload_file(file: UploadFile, request: Request) -> str:
    uploads_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'uploads'))
    os.makedirs(uploads_dir, exist_ok=True)
    extension = os.path.splitext(file.filename)[1]
    filename = f"{uuid4().hex}{extension}"
    file_path = os.path.join(uploads_dir, filename)
    with open(file_path, "wb") as dest:
        dest.write(file.file.read())
    base_url = str(request.base_url).rstrip("/")
    return f"{base_url}/uploads/{filename}"


async def _parse_request_data(request: Request) -> dict:
    content_type = request.headers.get("content-type", "")
    if content_type.startswith("multipart/form-data"):
        form = await request.form()
        data = {}
        for key, value in form.items():
            if isinstance(value, UploadFile):
                data[key] = value
            else:
                data[key] = value
        return data
    return await request.json()


@router.get("/", status_code=200)
def list_products(user=Depends(verifyToken)):
    return {"errCode": 0, "data": productService.list_products()}


@router.post("/create", status_code=201)
async def create_product(request: Request, user=Depends(verifyToken)):
    payload = await _parse_request_data(request)
    if "HinhAnh" in payload and hasattr(payload["HinhAnh"], "filename"):
        payload["HinhAnh"] = _save_upload_file(payload["HinhAnh"], request)
    result = productService.create_product(payload)
    return {"errCode": 0, "insertId": result}


@router.post("/update", status_code=200)
async def update_product(request: Request, user=Depends(verifyToken)):
    payload = await _parse_request_data(request)
    product_id = payload.get("MaSanPham")
    if not product_id:
        raise HTTPException(status_code=400, detail={"errCode": 1, "message": "Thiếu MaSanPham"})
    if "HinhAnh" in payload and hasattr(payload["HinhAnh"], "filename"):
        payload["HinhAnh"] = _save_upload_file(payload["HinhAnh"], request)
    affected = productService.update_product(product_id, payload)
    if affected == 0:
        raise HTTPException(status_code=404, detail={"errCode": 4, "message": "Product not found or no change"})
    return {"errCode": 0, "affected": affected}


@router.post("/delete", status_code=200)
def delete_products(payload: ProductActionRequest, user=Depends(verifyToken)):
    p_dict = payload.model_dump(exclude_unset=True)
    if "ids" in p_dict and p_dict["ids"]:
        ids = p_dict["ids"]
    elif "MaSanPham" in p_dict and p_dict["MaSanPham"]:
        ids = [p_dict["MaSanPham"]]
    elif "id" in p_dict and p_dict["id"]:
        ids = [p_dict["id"]]
    else:
        ids = None

    if not ids:
        raise HTTPException(status_code=400, detail={"errCode": 1, "message": "Thiếu danh sách sản phẩm"})
    
    deleted = productService.delete_products(ids)
    return {"errCode": 0, "deleted": deleted}


@router.post("/active", status_code=200)
def activate_product(payload: ProductActionRequest, user=Depends(verifyToken)):
    product_id = payload.id or payload.MaSanPham
    if not product_id:
        raise HTTPException(status_code=400, detail={"errCode": 1, "message": "Thiếu id"})
    activated = productService.activate_product(product_id)
    if activated == 0:
        raise HTTPException(status_code=404, detail={"errCode": 4, "message": "Product not found"})
    return {"errCode": 0, "activated": activated}



@router.get("/{product_id}", status_code=200)
def get_product(product_id: str, user=Depends(verifyToken)):
    prod = productService.get_product(product_id)
    if not prod:
        raise HTTPException(status_code=404, detail={"errCode": 4, "message": "Product not found"})
    return {"errCode": 0, "data": prod}
