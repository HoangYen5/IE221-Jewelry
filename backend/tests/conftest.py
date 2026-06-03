import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add the backend root to the sys path so we can import the app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from index import app

@pytest.fixture(scope="session")
def client():
    """Unauthenticated client fixture."""
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="session")
def admin_token(client):
    """Logs in with admin credentials and returns the JWT token."""
    response = client.post("/api/login", json={
        "TenTaiKhoan": "admin",
        "MatKhau": "123456"
    })
    assert response.status_code == 200
    data = response.json()
    assert data.get("errCode") == 0
    return data.get("token")

@pytest.fixture(scope="session")
def auth_client(admin_token):
    """Authenticated client fixture using admin token."""
    with TestClient(app) as c:
        c.headers.update({"Authorization": f"Bearer {admin_token}"})
        yield c
