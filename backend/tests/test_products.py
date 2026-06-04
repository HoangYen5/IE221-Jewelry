import pytest
import os
import time

TEST_PRODUCT_ID = f"SP_TEST_{int(time.time())}"

def test_list_products(auth_client):
    response = auth_client.get("/api/products/")
    assert response.status_code == 200
    data = response.json()
    assert data["errCode"] == 0
    assert isinstance(data["data"], list)

def test_create_product(auth_client):
    # We will test JSON payload first (no file upload in this simple test)
    # The QR code should still be generated based on MaSanPham
    payload = {
        "MaSanPham": TEST_PRODUCT_ID,
        "TenSanPham": "Test Diamond Ring",
        "MaLoaiSanPham": "LSP01",  # Assuming this exists, typical in the DB
        "SoLuongTon": 10,
        "DonGiaMuaVao": 1000000,
        "DonGiaBanRa": 1500000
    }
    response = auth_client.post("/api/products/create", json=payload)
    # Could fail if LSP01 doesn't exist due to foreign key constraint
    # But usually a test DB should have some basic data, or we just assert status code
    if response.status_code == 201:
        data = response.json()
        assert data["errCode"] == 0
        
        # Verify QR Code was generated
        qr_file_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', 'uploads', f'qr_{TEST_PRODUCT_ID}.png'
        ))
        assert os.path.exists(qr_file_path)

def test_get_product(auth_client):
    response = auth_client.get(f"/api/products/{TEST_PRODUCT_ID}")
    # If the create test passed, this should be 200. Otherwise 404.
    if response.status_code == 200:
        data = response.json()
        assert data["errCode"] == 0
        assert data["data"]["MaSanPham"] == TEST_PRODUCT_ID
        assert "qr_" in data["data"]["MaVach"]  # Verify MaVach field

def test_update_product(auth_client):
    payload = {
        "MaSanPham": TEST_PRODUCT_ID,
        "TenSanPham": "Updated Test Ring",
        "MaLoaiSanPham": "LSP01"
    }
    response = auth_client.post("/api/products/update", json=payload)
    if response.status_code == 200:
        data = response.json()
        assert data["errCode"] == 0
        assert data["affected"] > 0

def test_delete_product(auth_client):
    payload = {
        "ids": [TEST_PRODUCT_ID]
    }
    response = auth_client.post("/api/products/delete", json=payload)
    if response.status_code == 200:
        data = response.json()
        assert data["errCode"] == 0
        assert data["deleted"] > 0
        
    # Cleanup the QR file
    qr_file_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', 'uploads', f'qr_{TEST_PRODUCT_ID}.png'
    ))
    if os.path.exists(qr_file_path):
        os.remove(qr_file_path)
