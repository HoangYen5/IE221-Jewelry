# 💎 JewelryStore API — Backend Documentation

FastAPI backend for the **Jewelry Store Management System (IE221)**.  
Base URL: `http://localhost:8080`  
Interactive docs: `http://localhost:8080/docs` (Swagger UI)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- MySQL database

### Installation

```bash
# Clone and go to backend folder
cd backend

# Install dependencies
pip install -r requirements.txt

# Copy and fill in env variables
cp .env.example .env

# Run the server
python index.py
```

### Environment Variables (`.env`)

| Variable     | Description                  | Default         |
|--------------|------------------------------|-----------------|
| `DB_HOST`    | MySQL host                   | `127.0.0.1`     |
| `DB_USER`    | MySQL username               | `root`          |
| `DB_PASS`    | MySQL password               | *(empty)*       |
| `DB_NAME`    | MySQL database name          | `qlbh`          |
| `DB_PORT`    | MySQL port                   | `3306`          |
| `JWT_SECRET` | Secret key for JWT signing   | *(required)*    |
| `PORT`       | Port the server listens on   | `8080`          |

---

## 🔐 Authentication

All protected endpoints require a **JWT Bearer token** in the `Authorization` header:

```
Authorization: Bearer <token>
```

Tokens are obtained from the `/api/login` endpoint.

### Roles & Permissions

| Role      | Access Level                                  |
|-----------|-----------------------------------------------|
| `admin`   | Full access to all endpoints                  |
| `manager` | Most read/write operations (no employee mgmt) |
| `seller`  | Read access + create invoices/purchases/tickets |

---

## 📋 API Endpoints

---

### 🔑 Auth — `/api`

Authentication and password management.

#### `POST /api/login`
Authenticate user and obtain a JWT token.

- **Auth required:** No
- **Request body:**

```json
{
  "TenTaiKhoan": "admin",
  "MatKhau": "123456"
}
```

| Field          | Type   | Required | Description      |
|----------------|--------|----------|------------------|
| `TenTaiKhoan`  | string | ✅       | Username         |
| `MatKhau`      | string | ✅       | Password         |

- **Success response `200`:**

```json
{
  "errCode": 0,
  "token": "<jwt_token>",
  "user": { "TenTaiKhoan": "admin", "Role": "admin" }
}
```

---

#### `POST /api/change-password`
Change the current user's password.

- **Auth required:** Yes (any logged-in user)
- **Request body:**

```json
{
  "TenTaiKhoan": "admin",
  "MatKhauCu": "123456",
  "MatKhauMoi": "newpassword"
}
```

| Field          | Type   | Required | Description      |
|----------------|--------|----------|------------------|
| `TenTaiKhoan`  | string | ✅       | Username         |
| `MatKhauCu`    | string | ✅       | Current password |
| `MatKhauMoi`   | string | ✅       | New password     |

- **Success response `200`:** `{ "errCode": 0, "message": "Đổi mật khẩu thành công" }`

---

### 👤 Profile — `/api`

View the currently logged-in user's profile.

#### `GET /api/profile`
Get profile of the authenticated user from JWT token.

- **Auth required:** Yes (any role)
- **Success response `200`:** `{ "errCode": 0, "data": { ... } }`

#### `GET /api/get-all-profiles`
Alias endpoint for frontend compatibility — returns the same result as `/api/profile`.

- **Auth required:** Yes (any role)

---

### 📊 Dashboard — `/api/dashboard`

High-level statistics and chart data. **Restricted to `admin` and `manager`.**

#### `GET /api/dashboard/stats`
Returns summary KPIs: total products, customers, revenue, orders, etc.

- **Auth required:** Yes (`admin`, `manager`)
- **Purpose:** Power the main dashboard summary cards.

#### `GET /api/dashboard/revenue`
Returns monthly revenue data for charts.

- **Auth required:** Yes (`admin`, `manager`)
- **Purpose:** Render the revenue trend line/bar chart.

#### `GET /api/dashboard/category`
Returns product count grouped by category.

- **Auth required:** Yes (`admin`, `manager`)
- **Purpose:** Render the category distribution pie/donut chart.

#### `GET /api/dashboard/orders`
Returns recent order activity data.

- **Auth required:** Yes (`admin`, `manager`)
- **Purpose:** Display the recent orders chart or list on the dashboard.

---

### 📦 Products — `/api/products`

Full product lifecycle management including image upload and QR code generation.

#### `GET /api/products/`
List all products.

- **Auth required:** Yes (`admin`, `manager`, `seller`)
- **Purpose:** Display the product inventory list.

#### `GET /api/products/{product_id}`
Get details of a single product.

- **Auth required:** Yes (`admin`, `manager`, `seller`)
- **Path param:** `product_id` — Product code (e.g., `SP001`)

#### `POST /api/products/create`
Create a new product. Accepts `multipart/form-data` (for image upload) or JSON.  
Automatically generates a **QR code barcode** (`MaVach`) for the product.

- **Auth required:** Yes (`admin`, `manager`)
- **Content-Type:** `multipart/form-data` or `application/json`
- **Fields:**

| Field            | Type    | Required | Description                       |
|------------------|---------|----------|-----------------------------------|
| `MaSanPham`      | string  | Optional | Product code (auto-gen if omitted)|
| `TenSanPham`     | string  | ✅       | Product name                      |
| `MaLoaiSanPham`  | string  | ✅       | Product type/category code        |
| `SoLuongTon`     | integer | Optional | Stock quantity (default `0`)      |
| `DonGiaMuaVao`   | float   | Optional | Purchase price (default `0`)      |
| `DonGiaBanRa`    | float   | Optional | Selling price (default `0`)       |
| `HinhAnh`        | file    | Optional | Product image file                |

- **Success response `201`:** `{ "errCode": 0, "insertId": "<new_id>" }`

#### `POST /api/products/update`
Update an existing product. Accepts `multipart/form-data` or JSON.

- **Auth required:** Yes (`admin`, `manager`)
- **Fields:** Same as create. `MaSanPham` is **required**.

#### `POST /api/products/delete`
Soft-delete or hard-delete one or more products.

- **Auth required:** Yes (`admin`, `manager`)
- **Request body:**

```json
{ "ids": ["SP001", "SP002"] }
```

#### `POST /api/products/active`
Restore a soft-deleted product back to active status.

- **Auth required:** Yes (`admin`, `manager`)
- **Request body:** `{ "id": "SP001" }` or `{ "MaSanPham": "SP001" }`

---

### 🏷️ Categories — `/api`

Read-only lookup for product categories (loại sản phẩm). Used to populate dropdowns.

#### `GET /api/categories`
List all product categories.

- **Auth required:** Yes (`admin`, `manager`, `seller`)
- **Purpose:** Populate category filter/dropdown in the product form.

---

### 🗂️ Product Types — `/api/product-types`

Manage product types (loại sản phẩm) including profit margin and unit of measurement.

#### `GET /api/product-types/`
List all product types.

- **Auth required:** Yes (`admin`, `manager`, `seller`)

#### `POST /api/product-types/create`
Create a new product type.

- **Auth required:** Yes (`admin`, `manager`)
- **Request body:**

| Field               | Type   | Required | Description                              |
|---------------------|--------|----------|------------------------------------------|
| `MaLoaiSanPham`     | string | Optional | Type code (auto-generated if omitted)    |
| `TenLoaiSanPham`    | string | ✅       | Type name                                |
| `MaDVT`             | string | ✅       | Unit of measurement code                 |
| `PhanTramLoiNhuan`  | float  | Optional | Profit margin % (default `30`)           |

#### `POST /api/product-types/update`
Update a product type. `MaLoaiSanPham` is **required** in the body.

- **Auth required:** Yes (`admin`, `manager`)

#### `POST /api/product-types/delete`
Delete a product type by ID.

- **Auth required:** Yes (`admin`, `manager`)
- **Request body:** `{ "id": "LSP001" }` or `{ "MaLoaiSanPham": "LSP001" }`

---

### 👥 Customers — `/api/customers`

Customer CRUD management.

#### `GET /api/customers/`
List all customers.

- **Auth required:** Yes (`admin`, `manager`, `seller`)

#### `GET /api/customers/{customer_id}`
Get a specific customer.

- **Auth required:** Yes (`admin`, `manager`, `seller`)

#### `POST /api/customers/`
Create a new customer.

- **Auth required:** Yes (`admin`, `manager`, `seller`)
- **Request body:**

| Field           | Type   | Required | Description                          |
|-----------------|--------|----------|--------------------------------------|
| `MaKH`          | string | Optional | Customer code (auto-generated)       |
| `TenKH`         | string | ✅       | Customer name                        |
| `SoDienThoai`   | string | Optional | Phone number                         |
| `DiaChi`        | string | Optional | Address                              |

#### `PUT /api/customers/{customer_id}`
Update a customer.

- **Auth required:** Yes (`admin`, `manager`, `seller`)
- **Body fields:** Same as create (all optional on update).

#### `DELETE /api/customers/{customer_id}`
Delete a customer.

- **Auth required:** Yes (`admin`, `manager`, `seller`)

---

### 🏭 Suppliers — `/api/suppliers`

Supplier CRUD management.

#### `GET /api/suppliers/`
List all suppliers.

- **Auth required:** Yes (`admin`, `manager`, `seller`)

#### `GET /api/suppliers/{supplier_id}`
Get a specific supplier.

- **Auth required:** Yes (`admin`, `manager`, `seller`)

#### `POST /api/suppliers/`
Create a new supplier.

- **Auth required:** Yes (`admin`, `manager`)
- **Request body:**

| Field          | Type   | Required | Description                          |
|----------------|--------|----------|--------------------------------------|
| `MaNCC`        | string | Optional | Supplier code (auto-generated)       |
| `TenNCC`       | string | ✅       | Supplier name                        |
| `DiaChi`       | string | Optional | Address                              |
| `SoDienThoai`  | string | Optional | Phone number                         |

#### `PUT /api/suppliers/{supplier_id}`
Update a supplier.

- **Auth required:** Yes (`admin`, `manager`)

#### `DELETE /api/suppliers/{supplier_id}`
Delete a supplier.

- **Auth required:** Yes (`admin`, `manager`)

---

### 🧑‍💼 Employees — `/api/employees`

Manage employee accounts (system users). **Restricted to `admin` only.**

#### `GET /api/employees/`
List all employee accounts.

- **Auth required:** Yes (`admin`)

#### `GET /api/employees/{employee_id}`
Get a specific employee.

- **Auth required:** Yes (`admin`)

#### `POST /api/employees/`
Create a new employee account.

- **Auth required:** Yes (`admin`)
- **Request body:**

| Field          | Type   | Required | Description                       |
|----------------|--------|----------|-----------------------------------|
| `TenTaiKhoan`  | string | ✅       | Username / login name             |
| `MatKhau`      | string | ✅       | Initial password                  |
| `Role`         | string | Optional | `admin`, `manager`, `seller` (default: `seller`) |

#### `PUT /api/employees/{employee_id}`
Update an employee's account info or role.

- **Auth required:** Yes (`admin`)

#### `DELETE /api/employees/{employee_id}`
Delete an employee account.

- **Auth required:** Yes (`admin`)

---

### 🧾 Invoices (Sales Orders) — `/api/invoices`

Manage phiếu bán hàng (sales invoices) with line item details.

#### `GET /api/invoices/`
List all invoices.

- **Auth required:** Yes (`admin`, `manager`, `seller`)

#### `GET /api/invoices/{invoice_id}`
Get a specific invoice with its details.

- **Auth required:** Yes (`admin`, `manager`, `seller`)

#### `POST /api/invoices/create`
Create a new sales invoice with line items.

- **Auth required:** Yes (`admin`, `manager`, `seller`)
- **Request body:**

```json
{
  "SoPhieuBH": "PBH001",
  "NgayLap": "2024-06-01T00:00:00",
  "MaKH": "KH001",
  "TongTien": 5000000,
  "details": [
    {
      "MaSanPham": "SP001",
      "SoLuongBan": 2,
      "DonGiaBan": 2500000,
      "ThanhTien": 5000000
    }
  ]
}
```

| Field         | Type        | Required | Description                        |
|---------------|-------------|----------|------------------------------------|
| `SoPhieuBH`   | string      | Optional | Invoice number (auto-generated)    |
| `NgayLap`     | datetime    | Optional | Issue date                         |
| `MaKH`        | string      | ✅       | Customer code                      |
| `TongTien`    | float       | Optional | Total amount                       |
| `details`     | array       | Optional | List of sold items                 |

**Detail item fields:**

| Field          | Type    | Required | Description           |
|----------------|---------|----------|-----------------------|
| `MaSanPham`    | string  | ✅       | Product code          |
| `SoLuongBan`   | integer | ✅       | Quantity sold         |
| `DonGiaBan`    | float   | ✅       | Unit selling price    |
| `ThanhTien`    | float   | Optional | Line total            |

#### `POST /api/invoices/delete`
Delete one or more invoices.

- **Auth required:** Yes (`admin`, `manager`, `seller`)
- **Request body:** `{ "ids": ["PBH001", "PBH002"] }`

---

### 🛒 Purchases (Purchase Orders) — `/api/purchases`

Manage phiếu mua hàng (purchase orders from suppliers) with line item details.

#### `GET /api/purchases/`
List all purchase orders.

- **Auth required:** Yes (`admin`, `manager`, `seller`)

#### `GET /api/purchases/{purchase_id}`
Get a specific purchase order with its details.

- **Auth required:** Yes (`admin`, `manager`, `seller`)

#### `POST /api/purchases/create`
Create a new purchase order with line items.

- **Auth required:** Yes (`admin`, `manager`, `seller`)
- **Request body:**

```json
{
  "SoPhieuMH": "PMH001",
  "NgayLap": "2024-06-01T00:00:00",
  "MaNCC": "NCC001",
  "TongTien": 10000000,
  "details": [
    {
      "MaSanPham": "SP001",
      "SoLuongMua": 5,
      "DonGiaMua": 2000000,
      "ThanhTien": 10000000
    }
  ]
}
```

| Field        | Type     | Required | Description                            |
|--------------|----------|----------|----------------------------------------|
| `SoPhieuMH`  | string   | Optional | Purchase order number (auto-generated) |
| `NgayLap`    | datetime | Optional | Issue date                             |
| `MaNCC`      | string   | ✅       | Supplier code                          |
| `TongTien`   | float    | Optional | Total amount                           |
| `details`    | array    | Optional | List of purchased items                |

**Detail item fields:**

| Field         | Type    | Required | Description         |
|---------------|---------|----------|---------------------|
| `MaSanPham`   | string  | ✅       | Product code        |
| `SoLuongMua`  | integer | ✅       | Quantity purchased  |
| `DonGiaMua`   | float   | ✅       | Unit purchase price |
| `ThanhTien`   | float   | Optional | Line total          |

#### `POST /api/purchases/delete`
Delete one or more purchase orders.

- **Auth required:** Yes (`admin`, `manager`, `seller`)
- **Request body:** `{ "ids": ["PMH001"] }`

---

### 🔧 Service Tickets — `/api/service-tickets`

Manage phiếu dịch vụ (jewelry repair/service tickets) with status tracking and deposit support.

#### `GET /api/service-tickets/`
List all service tickets.

- **Auth required:** Yes (`admin`, `manager`, `seller`)

#### `GET /api/service-tickets/{ticket_id}`
Get a specific service ticket with its details.

- **Auth required:** Yes (`admin`, `manager`, `seller`)

#### `POST /api/service-tickets/create`
Create a new service ticket with service line items.

- **Auth required:** Yes (`admin`, `manager`, `seller`)
- **Request body:**

```json
{
  "SoPhieuDV": "PDV001",
  "NgayLap": "2024-06-01T00:00:00",
  "MaKH": "KH001",
  "TongTien": 500000,
  "TongTienTraTruoc": 200000,
  "TongTienConLai": 300000,
  "TinhTrang": "Đang xử lý",
  "details": [
    {
      "MaLoaiDV": "DV001",
      "DonGiaDuocTinh": 500000,
      "SoLuong": 1,
      "NgayGiao": "2024-06-10T00:00:00",
      "TinhTrang": "Chưa hoàn thành"
    }
  ]
}
```

| Field               | Type     | Required | Description                              |
|---------------------|----------|----------|------------------------------------------|
| `SoPhieuDV`         | string   | Optional | Ticket number (auto-generated)           |
| `NgayLap`           | datetime | Optional | Issue date                               |
| `MaKH`              | string   | ✅       | Customer code                            |
| `TongTien`          | float    | Optional | Total service cost                       |
| `TongTienTraTruoc`  | float    | Optional | Deposit amount paid upfront              |
| `TongTienConLai`    | float    | Optional | Remaining balance                        |
| `TinhTrang`         | string   | Optional | Ticket status (default: `"Đang xử lý"`) |
| `details`           | array    | Optional | List of service line items               |

**Detail item fields:**

| Field              | Type     | Required | Description                              |
|--------------------|----------|----------|------------------------------------------|
| `MaLoaiDV`         | string   | ✅       | Service type code                        |
| `DonGiaDuocTinh`   | float    | ✅       | Agreed unit price                        |
| `SoLuong`          | integer  | Optional | Quantity (default `1`)                   |
| `ThanhTien`        | float    | Optional | Line total                               |
| `TraTruoc`         | float    | Optional | Deposit for this line                    |
| `ConLai`           | float    | Optional | Remaining for this line                  |
| `NgayGiao`         | datetime | Optional | Expected delivery date                   |
| `TinhTrang`        | string   | Optional | Status (default: `"Chưa hoàn thành"`)   |

#### `POST /api/service-tickets/status`
Update only the status of a service ticket.

- **Auth required:** Yes (`admin`, `manager`, `seller`)
- **Request body:**

```json
{ "id": "PDV001", "status": "Hoàn thành" }
```

#### `POST /api/service-tickets/delete`
Delete one or more service tickets.

- **Auth required:** Yes (`admin`, `manager`, `seller`)
- **Request body:** `{ "ids": ["PDV001"] }`

---

### 🛠️ Service Types — `/api/service-types`

Manage types of jewelry services (e.g., polishing, resizing, engraving).

#### `GET /api/service-types/`
List all service types.

- **Auth required:** Yes (`admin`, `manager`, `seller`)

#### `POST /api/service-types/create`
Create a new service type.

- **Auth required:** Yes (`admin`, `manager`)
- **Request body:**

| Field               | Type   | Required | Description                              |
|---------------------|--------|----------|------------------------------------------|
| `MaLoaiDV`          | string | Optional | Service type code (auto-generated)       |
| `TenLoaiDV`         | string | ✅       | Service type name                        |
| `DonGiaDV`          | float  | Optional | Default unit price (default `0`)         |
| `PhanTramTraTruoc`  | float  | Optional | Default deposit % (default `0.5` = 50%) |

#### `POST /api/service-types/update`
Update a service type. `MaLoaiDV` is **required** in the body.

- **Auth required:** Yes (`admin`, `manager`)

#### `POST /api/service-types/delete`
Delete a service type.

- **Auth required:** Yes (`admin`, `manager`)
- **Request body:** `{ "id": "DV001" }` or `{ "MaLoaiDV": "DV001" }`

---

### 📏 Units of Measurement — `/api/units`

Manage đơn vị tính (units) used in product types.

#### `GET /api/units/`
List all units of measurement.

- **Auth required:** Yes (`admin`, `manager`, `seller`)

#### `GET /api/units/search?q={keyword}`
Search units by keyword.

- **Auth required:** Yes (`admin`, `manager`, `seller`)
- **Query param:** `q` — search keyword string

#### `GET /api/units/next-code`
Get the next auto-generated unit code (for pre-filling forms).

- **Auth required:** Yes (`admin`, `manager`, `seller`)

#### `GET /api/units/{unit_id}`
Get a specific unit of measurement.

- **Auth required:** Yes (`admin`, `manager`, `seller`)

#### `POST /api/units/`
Create a new unit of measurement.

- **Auth required:** Yes (`admin`, `manager`)
- **Request body:**

| Field    | Type   | Required | Description                        |
|----------|--------|----------|------------------------------------|
| `MaDVT`  | string | Optional | Unit code (auto-generated)         |
| `TenDVT` | string | ✅       | Unit name (e.g., `"Chiếc"`, `"Gram"`) |

#### `PUT /api/units/{unit_id}`
Update a unit of measurement.

- **Auth required:** Yes (`admin`, `manager`)

#### `DELETE /api/units/{unit_id}`
Delete a unit of measurement.

- **Auth required:** Yes (`admin`, `manager`)

---

### 📈 Reports — `/api/report`

Inventory reporting by month and year. **Restricted to `admin` and `manager`.**

#### `GET /api/report/`
Get all inventory report entries, with optional filters.

- **Auth required:** Yes (`admin`, `manager`)
- **Query params:**

| Param   | Type    | Required | Description       |
|---------|---------|----------|-------------------|
| `month` | integer | Optional | Filter by month   |
| `year`  | integer | Optional | Filter by year    |

- **Example:** `GET /api/report/?month=6&year=2024`

#### `GET /api/report/{thang}/{nam}/{ma_san_pham}`
Get a single inventory report row by month, year, and product.

- **Auth required:** Yes (`admin`, `manager`)
- **Path params:**
  - `thang` — Month (integer)
  - `nam` — Year (integer)
  - `ma_san_pham` — Product code (string)

#### `POST /api/report/create`
Create a new inventory report entry. Returns `409` if the same month/year/product combination already exists.

- **Auth required:** Yes (`admin`, `manager`)
- **Request body:**

| Field           | Type    | Required | Description                  |
|-----------------|---------|----------|------------------------------|
| `Thang`         | integer | ✅       | Month (1–12)                 |
| `Nam`           | integer | ✅       | Year (e.g., `2024`)          |
| `MaSanPham`     | string  | ✅       | Product code                 |
| `TonDau`        | integer | Optional | Opening stock (default `0`)  |
| `SoLuongMuaVao` | integer | Optional | Quantity purchased            |
| `SoLuongBanRa`  | integer | Optional | Quantity sold                |
| `TonCuoi`       | integer | Optional | Closing stock (default `0`)  |

---

## 🗂️ Static Files

Product images and QR codes are served as static files:

```
GET /uploads/<filename>
```

Files are stored in `backend/uploads/`.

---

## 📁 Project Structure

```
backend/
├── index.py              # FastAPI app entry point, router registration
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variable template
├── Dockerfile
├── docker-compose.yml
└── src/
    ├── config/
    │   └── connectDB.py  # MySQL connection setup
    ├── middleware/
    │   └── authMiddleware.py  # JWT verify + role check
    ├── models/           # DB query logic (one file per entity)
    ├── routes/           # FastAPI routers (one file per entity)
    ├── schemas/          # Pydantic request/response models
    ├── service/          # Business logic layer
    └── utils/            # Utilities (QR code gen, file upload, etc.)
```

---

## 🛡️ Error Response Format

All errors follow a consistent format:

```json
{
  "errCode": 1,
  "message": "Error description"
}
```

| `errCode` | Meaning                         |
|-----------|---------------------------------|
| `0`       | Success                         |
| `1`       | Missing / invalid input         |
| `2`       | Auth / duplicate conflict       |
| `3`       | Insufficient permissions        |
| `4`       | Resource not found              |

---

## 🧪 Running Tests

```bash
cd backend
pytest tests/
```

---

## 🐳 Docker

```bash
# Build and start
docker-compose up --build

# Stop
docker-compose down
```
