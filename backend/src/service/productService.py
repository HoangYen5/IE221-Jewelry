import os
import qrcode
from uuid import uuid4
from fastapi import UploadFile
from ..models import productModel

UPLOADS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'uploads')
)


def save_upload_file(file: UploadFile, base_url: str) -> str:
    """Save an uploaded image file to disk and return its public URL."""
    os.makedirs(UPLOADS_DIR, exist_ok=True)
    extension = os.path.splitext(file.filename)[1]
    filename = f"{uuid4().hex}{extension}"
    file_path = os.path.join(UPLOADS_DIR, filename)
    with open(file_path, "wb") as dest:
        dest.write(file.file.read())
    return f"{base_url}/uploads/{filename}"


def generate_qr_code(product_id: str, base_url: str) -> str:
    """Generate a QR code image for a product and return its public URL."""
    os.makedirs(UPLOADS_DIR, exist_ok=True)
    filename = f"qr_{product_id}.png"
    file_path = os.path.join(UPLOADS_DIR, filename)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(product_id)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)

    return f"{base_url}/uploads/{filename}"

def list_products():
    return productModel.getAllProducts()

def list_categories():
    return productModel.getAllCategories()

def get_product(product_id):
    return productModel.getProductById(product_id)

def create_product(data: dict):
    return productModel.createProduct(data)

def update_product(product_id, data: dict):
    return productModel.updateProduct(product_id, data)

def delete_product(product_id):
    return productModel.deleteProduct(product_id)

def activate_product(product_id):
    return productModel.activateProduct(product_id)

def delete_products(product_ids):
    return productModel.deleteProducts(product_ids)
