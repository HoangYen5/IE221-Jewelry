from ..config.connectDB import get_connection

def findUserByUsername(username):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM TAIKHOAN WHERE TenTaiKhoan = %s', (username,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()


def authenticateUser(username, password):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            'SELECT * FROM TAIKHOAN WHERE TenTaiKhoan = %s AND MatKhau = %s',
            (username, password),
        )
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()


def updatePassword(username, new_password):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE TAIKHOAN SET MatKhau = %s WHERE TenTaiKhoan = %s',
            (new_password, username),
        )
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
