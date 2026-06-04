from ..config.connectDB import get_connection
from ..utils.utils import generate_id

def getAllCustomers():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM khachhang')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def getCustomerById(customer_id):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM khachhang WHERE MaKH = %s', (customer_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def createCustomer(data: dict):
    if not data:
        return None
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        if 'MaKH' not in data or not data['MaKH']:
            data['MaKH'] = generate_id(cursor, 'khachhang', 'MaKH', 'KH')
            
        cols = ','.join(data.keys())
        placeholders = ','.join(['%s'] * len(data))
        values = tuple(data.values())
        query = f"INSERT INTO khachhang ({cols}) VALUES ({placeholders})"
        
        cursor.execute(query, values)
        conn.commit()
        return data.get('MaKH')
    finally:
        cursor.close()
        conn.close()

def updateCustomer(customer_id, data: dict):
    if not data:
        return 0
    set_clause = ','.join([f"{k} = %s" for k in data.keys()])
    values = list(data.values()) + [customer_id]
    query = f"UPDATE khachhang SET {set_clause} WHERE MaKH = %s"
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, tuple(values))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def deleteCustomer(customer_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM khachhang WHERE MaKH = %s', (customer_id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
