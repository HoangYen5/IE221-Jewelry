from ..config.connectDB import get_connection

def getDashboardStats():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT 1 AS dummy')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
