from ..config.connectDB import get_connection

def getProfile(user_id):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM profile WHERE id = %s', (user_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()
