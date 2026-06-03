import pytest

@pytest.mark.parametrize("endpoint", [
    "/api/dashboard/stats",
    "/api/dashboard/revenue",
    "/api/dashboard/category",
    "/api/dashboard/orders",
    "/api/employees/",
    "/api/categories/categories",  # Actually the route is /api/categories
    "/api/product-types/",
    "/api/units/",
    "/api/service-types/",
    "/api/invoices/",
    "/api/customers/",
    "/api/purchases/",
    "/api/suppliers/",
    "/api/service-tickets/"
])
def test_general_get_endpoints_authorized(auth_client, endpoint):
    """
    Test that an authorized admin can access all basic GET list endpoints
    without throwing a 500 or 403 error.
    """
    response = auth_client.get(endpoint)
    # The categories route is slightly different in the app structure
    if endpoint == "/api/categories/categories" and response.status_code == 404:
        response = auth_client.get("/api/categories")
        
    assert response.status_code == 200
    data = response.json()
    assert data["errCode"] == 0
    assert "data" in data

@pytest.mark.parametrize("endpoint", [
    "/api/dashboard/stats",
    "/api/employees/",
    "/api/invoices/"
])
def test_general_get_endpoints_unauthorized(client, endpoint):
    """
    Test that an unauthorized user cannot access protected endpoints.
    """
    response = client.get(endpoint)
    assert response.status_code == 403
    data = response.json()
    assert "detail" in data
