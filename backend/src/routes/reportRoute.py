from ..schemas.reportSchema import ReportCreate, ReportResponse
from fastapi import APIRouter, Depends, HTTPException
from ..service import reportService
from ..middleware.authMiddleware import checkPermission

router = APIRouter(prefix="/api/report", tags=["reports"])


@router.get("/", status_code=200)
def get_report(month: int = None, year: int = None, user=Depends(checkPermission(["admin", "manager"]))):
    """Get all inventory reports, optionally filtered by month and/or year."""
    params = {}
    if month is not None:
        params['month'] = month
    if year is not None:
        params['year'] = year
    return {"errCode": 0, "data": reportService.get_report(params if params else None)}


@router.get("/{thang}/{nam}/{ma_san_pham}", status_code=200)
def get_report_by_id(thang: int, nam: int, ma_san_pham: str, user=Depends(checkPermission(["admin", "manager"]))):
    """Get a specific inventory report row by month, year and product code."""
    row = reportService.get_report_by_id(thang, nam, ma_san_pham)
    if not row:
        raise HTTPException(status_code=404, detail={"errCode": 4, "message": "Không tìm thấy báo cáo"})
    return {"errCode": 0, "data": row}


@router.post("/create", status_code=201)
def create_report(payload: ReportCreate, user=Depends(checkPermission(["admin", "manager"]))):
    """Create a new inventory report row. Skips silently if the same (Thang/Nam/MaSanPham) already exists."""
    rows = reportService.create_report(payload.model_dump())
    if rows == 0:
        raise HTTPException(status_code=409, detail={"errCode": 2, "message": "Báo cáo đã tồn tại cho tháng/năm/sản phẩm này"})
    return {"errCode": 0, "affected": rows}
