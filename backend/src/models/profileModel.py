from ..config.connectDB import get_connection

def getProfile(username):
    """Get profile by username (from JWT token)."""
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            'SELECT MaTaiKhoan, TenTaiKhoan, Role, createdAt FROM TAIKHOAN WHERE TenTaiKhoan = %s',
            (username,)
        )
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()
