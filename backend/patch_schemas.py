import os

# Patch invoiceSchema.py
with open("/home/hnim3107/Data/Projects/IE221-Jewelry/backend/src/schemas/invoiceSchema.py", "a") as f:
    f.write("""
class InvoiceDetail(BaseModel):
    MaSanPham: str
    SoLuongBan: int
    DonGiaBan: float
    ThanhTien: Optional[float] = None

class InvoiceCreate(InvoiceBase):
    details: Optional[List[InvoiceDetail]] = None
    
# Re-define InvoiceCreate to override the old one
""")

# Actually let's use a Python script to rewrite those files properly.
