from ..config.connectDB import get_connection

def getAllInvoices():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM hoadon')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def getInvoiceById(invoice_id):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM hoadon WHERE MaHoaDon = %s', (invoice_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def createInvoice(data: dict):
    if not data:
        return None
    cols = ','.join(data.keys())
    placeholders = ','.join(['%s'] * len(data))
    values = tuple(data.values())
    query = f"INSERT INTO hoadon ({cols}) VALUES ({placeholders})"
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        conn.close()

def updateInvoice(invoice_id, data: dict):
    if not data:
        return 0
    set_clause = ','.join([f"{k} = %s" for k in data.keys()])
    values = list(data.values()) + [invoice_id]
    query = f"UPDATE hoadon SET {set_clause} WHERE MaHoaDon = %s"
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, tuple(values))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def deleteInvoice(invoice_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM hoadon WHERE MaHoaDon = %s', (invoice_id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
