def test_login_success(client):
    response = client.post("/api/login", json={
        "TenTaiKhoan": "admin",
        "MatKhau": "123456"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["errCode"] == 0
    assert "token" in data
    assert "user" in data
    assert data["user"]["TenTaiKhoan"] == "admin"
    assert data["user"]["Role"] == "admin"

def test_login_invalid_credentials(client):
    response = client.post("/api/login", json={
        "TenTaiKhoan": "admin",
        "MatKhau": "wrongpassword"
    })
    assert response.status_code == 401
    data = response.json()
    assert data["detail"]["errCode"] == 1

def test_change_password_unauthorized(client):
    response = client.post("/api/change-password", json={
        "TenTaiKhoan": "admin",
        "MatKhauCu": "123456",
        "MatKhauMoi": "123123"
    })
    assert response.status_code == 403  # verifyToken raises 403

def test_change_password_authorized_but_wrong_old(auth_client):
    response = auth_client.post("/api/change-password", json={
        "TenTaiKhoan": "admin",
        "MatKhauCu": "wrongold",
        "MatKhauMoi": "123123"
    })
    assert response.status_code == 401
    data = response.json()
    assert data["detail"]["errCode"] == 2
