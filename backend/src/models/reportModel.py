from ..config.connectDB import get_connection

def getReport(params=None):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT 1 AS ok')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
