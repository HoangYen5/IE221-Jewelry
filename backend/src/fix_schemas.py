from datetime import datetime

files = {
    'categorySchema.py': """from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class CategoryBase(BaseModel):
    TenLoaiSanPham: str
    MaDVT: str
    PhanTramLoiNhuan: Optional[float] = 30

class CategoryCreate(CategoryBase):
    MaLoaiSanPham: Optional[str] = None

class CategoryUpdate(CategoryBase):
    TenLoaiSanPham: Optional[str] = None
    MaDVT: Optional[str] = None
    PhanTramLoiNhuan: Optional[float] = None

class CategoryResponse(CategoryBase):
    MaLoaiSanPham: str
    createdAt: Optional[datetime] = None
""",
    'customerSchema.py': """from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class CustomerBase(BaseModel):
    TenKH: str
    SoDienThoai: Optional[str] = None
    DiaChi: Optional[str] = None

class CustomerCreate(CustomerBase):
    MaKH: Optional[str] = None

class CustomerUpdate(CustomerBase):
    TenKH: Optional[str] = None

class CustomerResponse(CustomerBase):
    MaKH: str
    createdAt: Optional[datetime] = None
""",
    'invoiceSchema.py': """from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class InvoiceBase(BaseModel):
    NgayLap: Optional[datetime] = None
    MaKH: str
    TongTien: Optional[float] = 0

class InvoiceDetail(BaseModel):
    MaSanPham: str
    SoLuongBan: int
    DonGiaBan: float
    ThanhTien: Optional[float] = 0

class InvoiceCreate(InvoiceBase):
    SoPhieuBH: Optional[str] = None
    details: Optional[List[InvoiceDetail]] = None

class InvoiceUpdate(InvoiceBase):
    MaKH: Optional[str] = None
    details: Optional[List[InvoiceDetail]] = None

class InvoiceResponse(InvoiceBase):
    SoPhieuBH: str
    details: Optional[List[InvoiceDetail]] = None
""",
    'productTypeSchema.py': """from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class ProductTypeBase(BaseModel):
    TenLoaiSanPham: str
    MaDVT: str
    PhanTramLoiNhuan: Optional[float] = 30

class ProductTypeCreate(ProductTypeBase):
    MaLoaiSanPham: Optional[str] = None

class ProductTypeUpdate(ProductTypeBase):
    TenLoaiSanPham: Optional[str] = None
    MaDVT: Optional[str] = None
    PhanTramLoiNhuan: Optional[float] = None

class ProductTypeResponse(ProductTypeBase):
    MaLoaiSanPham: str
    createdAt: Optional[datetime] = None
""",
    'purchaseSchema.py': """from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PurchaseBase(BaseModel):
    NgayLap: Optional[datetime] = None
    MaNCC: str
    TongTien: Optional[float] = 0

class PurchaseDetail(BaseModel):
    MaSanPham: str
    SoLuongMua: int
    DonGiaMua: float
    ThanhTien: Optional[float] = 0

class PurchaseCreate(PurchaseBase):
    SoPhieuMH: Optional[str] = None
    details: Optional[List[PurchaseDetail]] = None

class PurchaseUpdate(PurchaseBase):
    MaNCC: Optional[str] = None
    details: Optional[List[PurchaseDetail]] = None

class PurchaseResponse(PurchaseBase):
    SoPhieuMH: str
    details: Optional[List[PurchaseDetail]] = None
""",
    'serviceTicketSchema.py': """from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ServiceTicketBase(BaseModel):
    NgayLap: Optional[datetime] = None
    MaKH: str
    TongTien: Optional[float] = 0
    TongTienTraTruoc: Optional[float] = 0
    TongTienConLai: Optional[float] = 0
    TinhTrang: Optional[str] = 'Đang xử lý'

class ServiceTicketDetail(BaseModel):
    MaLoaiDV: str
    DonGiaDuocTinh: float
    SoLuong: int = 1
    ThanhTien: Optional[float] = 0
    TraTruoc: Optional[float] = 0
    ConLai: Optional[float] = 0
    NgayGiao: Optional[datetime] = None
    TinhTrang: Optional[str] = 'Chưa hoàn thành'

class ServiceticketCreate(ServiceTicketBase):
    SoPhieuDV: Optional[str] = None
    details: Optional[List[ServiceTicketDetail]] = None

class ServiceticketUpdate(ServiceTicketBase):
    MaKH: Optional[str] = None
    TinhTrang: Optional[str] = None
    details: Optional[List[ServiceTicketDetail]] = None

class ServiceticketResponse(ServiceTicketBase):
    SoPhieuDV: str
    details: Optional[List[ServiceTicketDetail]] = None
""",
    'serviceTypeSchema.py': """from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class ServiceTypeBase(BaseModel):
    TenLoaiDV: str
    DonGiaDV: Optional[float] = 0
    PhanTramTraTruoc: Optional[float] = 0.5

class ServicetypeCreate(ServiceTypeBase):
    MaLoaiDV: Optional[str] = None

class ServicetypeUpdate(ServiceTypeBase):
    TenLoaiDV: Optional[str] = None
    DonGiaDV: Optional[float] = None
    PhanTramTraTruoc: Optional[float] = None

class ServicetypeResponse(ServiceTypeBase):
    MaLoaiDV: str
    createdAt: Optional[datetime] = None
""",
    'supplierSchema.py': """from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class SupplierBase(BaseModel):
    TenNCC: str
    DiaChi: Optional[str] = None
    SoDienThoai: Optional[str] = None

class SupplierCreate(SupplierBase):
    MaNCC: Optional[str] = None

class SupplierUpdate(SupplierBase):
    TenNCC: Optional[str] = None

class SupplierResponse(SupplierBase):
    MaNCC: str
    createdAt: Optional[datetime] = None
""",
    'unitSchema.py': """from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class UnitBase(BaseModel):
    TenDVT: str

class UnitCreate(UnitBase):
    MaDVT: Optional[str] = None

class UnitUpdate(UnitBase):
    TenDVT: Optional[str] = None

class UnitResponse(UnitBase):
    MaDVT: str
    createdAt: Optional[datetime] = None
""",
    'productSchema.py': """from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class ProductBase(BaseModel):
    TenSanPham: str
    MaLoaiSanPham: str
    SoLuongTon: Optional[int] = 0
    DonGiaMuaVao: Optional[float] = 0
    DonGiaBanRa: Optional[float] = 0
    HinhAnh: Optional[str] = None
    MaVach: Optional[str] = None
    isDelete: Optional[bool] = False

class ProductCreate(ProductBase):
    MaSanPham: Optional[str] = None

class ProductUpdate(ProductBase):
    TenSanPham: Optional[str] = None
    MaLoaiSanPham: Optional[str] = None
    SoLuongTon: Optional[int] = None
    DonGiaMuaVao: Optional[float] = None
    DonGiaBanRa: Optional[float] = None
    HinhAnh: Optional[str] = None
    MaVach: Optional[str] = None
    isDelete: Optional[bool] = None

class ProductResponse(ProductBase):
    MaSanPham: str
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class ProductActionRequest(BaseModel):
    id: Optional[str] = None
    MaSanPham: Optional[str] = None
    ids: Optional[List[str]] = None
""",
}

for name, content in files.items():
    with open('/home/hnim3107/Data/Projects/IE221-Jewelry/backend/src/schemas/' + name, 'w') as f:
        f.write(content)

print("Refactored schemas.")
