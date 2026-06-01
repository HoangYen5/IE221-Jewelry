from ..config.connectDB import get_connection

def getAllServiceTypes():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM loaidichvu')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
