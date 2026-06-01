from ..config.connectDB import get_connection

def getAllServiceTickets():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM phieudichvu')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
