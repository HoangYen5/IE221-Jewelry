from ..config.connectDB import get_connection

def getAllPurchases():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM phieunhap')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def getPurchaseById(purchase_id):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM phieunhap WHERE MaPhieuNhap = %s', (purchase_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def createPurchase(data: dict):
    if not data:
        return None
    cols = ','.join(data.keys())
    placeholders = ','.join(['%s'] * len(data))
    values = tuple(data.values())
    query = f"INSERT INTO phieunhap ({cols}) VALUES ({placeholders})"
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        conn.close()

def updatePurchase(purchase_id, data: dict):
    if not data:
        return 0
    set_clause = ','.join([f"{k} = %s" for k in data.keys()])
    values = list(data.values()) + [purchase_id]
    query = f"UPDATE phieunhap SET {set_clause} WHERE MaPhieuNhap = %s"
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, tuple(values))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def deletePurchase(purchase_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM phieunhap WHERE MaPhieuNhap = %s', (purchase_id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
