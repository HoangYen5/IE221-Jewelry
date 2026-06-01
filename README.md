# JewelryStore

Hệ thống quản lý cửa hàng vàng bạc đá quý (JewelryStore) gồm:
- Backend: Python + FastAPI
- Frontend: React + Vite
- Database: MySQL

## Tổng quan

Dự án này xây dựng một ứng dụng quản lý bán hàng cho cửa hàng trang sức. Backend cung cấp REST API, frontend hiển thị giao diện quản lý đơn hàng, khách hàng, nhân viên, sản phẩm, hóa đơn, nhập hàng, dịch vụ bảo trì và báo cáo.

## Kiến trúc

- Backend: `backend/`
  - Python FastAPI
  - Sử dụng `uvicorn` để chạy server
  - Kết nối MySQL qua `backend/src/config/connectDB.py`
  - Tải file cấu hình từ `.env`
- Frontend: `frontend/`
  - React + Vite
  - Redux Toolkit + Ant Design
  - Gọi API qua `frontend/src/services/axios.js`
- Database: MySQL
  - Tên database mặc định: `qlbh`
  - File seed mẫu: `backend/src/sql/data.sql`

## Yêu cầu

- Windows hoặc hệ điều hành tương thích
- Python 3.8+ (đề xuất 3.11+)
- MySQL hoặc XAMPP
- Node.js 18+ và npm
- Git (nên có nhưng không bắt buộc)

## Cấu trúc thư mục chính

- `backend/`
  - `index.py`: entrypoint backend
  - `.env.example`: mẫu biến môi trường backend
  - `requirements.txt`: thư viện Python backend
  - `setup_env.ps1`: tạo virtual environment và cài đặt dependency
  - `run_backend.ps1`: chạy server backend
  - `src/`: mã nguồn backend
    - `config/`: cấu hình DB
    - `routes/`: định nghĩa router REST API
    - `service/`: logic nghiệp vụ
    - `models/`: model dữ liệu
- `frontend/`
  - `package.json`: config frontend
  - `src/`: mã nguồn React
    - `routes/`, `components/`, `redux/`, `services/`, `page/`
  - `.env.example`: biến môi trường frontend

## Thiết lập database

1. Khởi động MySQL hoặc XAMPP.
2. Tạo database tên `qlbh`.
3. Import file dữ liệu mẫu:
   - `backend/src/sql/data.sql`
4. Nếu cần, cập nhật thông tin kết nối trong file `.env` của backend.

## Cài đặt và chạy Backend

1. Mở terminal và chuyển đến thư mục backend:
   ```powershell
   cd backend
   ```
2. Thiết lập môi trường ảo và cài dependency:
   ```powershell
   .\setup_env.ps1
   ```
3. Kiểm tra file `.env` đã tồn tại hay chưa.
   - Nếu chưa có, script sẽ tự động copy từ `.env.example`.
4. Mở `.env` và cập nhật thông tin MySQL và JWT:
   ```text
   DB_HOST=127.0.0.1
   DB_USER=root
   DB_PASS=
   DB_NAME=qlbh
   DB_PORT=3306
   JWT_SECRET=your_jwt_secret_here
   PORT=8080
   ```
5. Chạy backend:
   ```powershell
   .\run_backend.ps1
   ```

> Nếu muốn chạy trực tiếp mà không dùng script:
> `backend\.venv\Scripts\python.exe -m uvicorn index:app --reload --port 8080`

## Cài đặt và chạy Frontend

1. Mở terminal mới và chuyển đến thư mục frontend:
   ```powershell
   cd frontend
   ```
2. Cài đặt dependency:
   ```powershell
   npm install
   ```
3. Chạy ứng dụng frontend:
   ```powershell
   npm run dev
   ```
4. Mở trình duyệt theo URL Vite cung cấp, mặc định là:
   - `http://localhost:5173`

## Biến môi trường

### Backend
- `backend/.env.example` chứa cấu hình mẫu:
  - `DB_HOST`
  - `DB_USER`
  - `DB_PASS`
  - `DB_NAME`
  - `DB_PORT`
  - `JWT_SECRET`
  - `PORT`

### Frontend
- `frontend/.env.example` chứa:
  - `VITE_API_URL=http://localhost:8080`

Frontend sử dụng giá trị `VITE_API_URL` để trỏ tới backend.

## Endpoints chính

Backend cung cấp API theo router trong `backend/src/routes/`.

Một số endpoint phổ biến:

- `POST /api/login`
- `POST /api/change-password`
- `GET /api/products`
- `POST /api/products/create`
- `POST /api/products/update`
- `POST /api/products/delete`
- `POST /api/products/active`
- `GET /api/products/{product_id}`
- `GET /api/categories`

## Test API nhanh

1. Chạy backend.
2. Gửi request `POST http://localhost:8080/api/login`.
3. Body JSON ví dụ:
   ```json
   {
     "username": "admin",
     "password": "123456"
   }
   ```
4. Lấy token trả về và thêm header `Authorization: Bearer <token>` cho các request cần xác thực.

## Lưu ý quan trọng

- Backend chạy mặc định tại `http://localhost:8080`.
- Frontend chạy mặc định tại `http://localhost:5173`.
- Nếu thay đổi port backend, cập nhật `frontend/src/services/axios.js` và `frontend/.env`.
- Ảnh upload tạm được phục vụ từ `backend/uploads`.

## Bổ sung

- FastAPI cung cấp API docs tại `http://localhost:8080/docs` khi backend đang chạy.
- Root backend trả về JSON:
  ```json
  {"message": "Server đang chạy (Python)"}
  ```

---
