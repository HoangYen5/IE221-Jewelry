from fastapi import APIRouter, Depends, HTTPException, Request, UploadFile
from ..service import productService
from ..middleware.authMiddleware import checkPermission
from ..schemas.productSchema import ProductActionRequest

router = APIRouter(prefix="/api/products", tags=["products"])


async def _parse_request_data(request: Request) -> dict:
    """Parse multipart/form-data or JSON body into a plain dict."""
    content_type = request.headers.get("content-type", "")
    if content_type.startswith("multipart/form-data"):
        form = await request.form()
        return {key: value for key, value in form.items()}
    return await request.json()


@router.get("/", status_code=200)
def list_products(user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Get a list of all products."""
    return {"errCode": 0, "data": productService.list_products()}


@router.post("/create", status_code=201)
async def create_product(request: Request, user=Depends(checkPermission(["admin", "manager"]))):
    """Create a new product. Automatically generates and stores a QR code."""
    payload = await _parse_request_data(request)
    base_url = str(request.base_url).rstrip("/")

    # Delegate file handling to the service layer
    if "HinhAnh" in payload and hasattr(payload["HinhAnh"], "filename"):
        payload["HinhAnh"] = productService.save_upload_file(payload["HinhAnh"], base_url)

    # Delegate QR code generation to the service layer
    product_id = payload.get("MaSanPham")
    if product_id:
        payload["MaVach"] = productService.generate_qr_code(product_id, base_url)

    result = productService.create_product(payload)
    return {"errCode": 0, "insertId": result}


@router.post("/update", status_code=200)
async def update_product(request: Request, user=Depends(checkPermission(["admin", "manager"]))):
    """Update an existing product."""
    payload = await _parse_request_data(request)
    product_id = payload.get("MaSanPham")
    if not product_id:
        raise HTTPException(status_code=400, detail={"errCode": 1, "message": "Thiếu MaSanPham"})

    base_url = str(request.base_url).rstrip("/")
    if "HinhAnh" in payload and hasattr(payload["HinhAnh"], "filename"):
        payload["HinhAnh"] = productService.save_upload_file(payload["HinhAnh"], base_url)

    affected = productService.update_product(product_id, payload)
    if affected == 0:
        raise HTTPException(status_code=404, detail={"errCode": 4, "message": "Product not found or no change"})
    return {"errCode": 0, "affected": affected}


@router.post("/delete", status_code=200)
def delete_products(payload: ProductActionRequest, user=Depends(checkPermission(["admin", "manager"]))):
    """Delete one or more products (soft or hard delete based on status)."""
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
def activate_product(payload: ProductActionRequest, user=Depends(checkPermission(["admin", "manager"]))):
    """Restore a soft-deleted product."""
    product_id = payload.id or payload.MaSanPham
    if not product_id:
        raise HTTPException(status_code=400, detail={"errCode": 1, "message": "Thiếu id"})
    activated = productService.activate_product(product_id)
    if activated == 0:
        raise HTTPException(status_code=404, detail={"errCode": 4, "message": "Product not found"})
    return {"errCode": 0, "activated": activated}


@router.get("/{product_id}", status_code=200)
def get_product(product_id: str, user=Depends(checkPermission(["admin", "manager", "seller"]))):
    """Get details of a specific product."""
    prod = productService.get_product(product_id)
    if not prod:
        raise HTTPException(status_code=404, detail={"errCode": 4, "message": "Product not found"})
    return {"errCode": 0, "data": prod}
