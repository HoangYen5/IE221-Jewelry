from ..config.connectDB import get_connection

def getAllProductTypes():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM loaisanpham')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
