from ..config.connectDB import get_connection

def getAllSuppliers():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM nhacungcap')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def getSupplierById(supplier_id):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM nhacungcap WHERE MaNhaCungCap = %s', (supplier_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def createSupplier(data: dict):
    if not data:
        return None
    cols = ','.join(data.keys())
    placeholders = ','.join(['%s'] * len(data))
    values = tuple(data.values())
    query = f"INSERT INTO nhacungcap ({cols}) VALUES ({placeholders})"
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        conn.close()

def updateSupplier(supplier_id, data: dict):
    if not data:
        return 0
    set_clause = ','.join([f"{k} = %s" for k in data.keys()])
    values = list(data.values()) + [supplier_id]
    query = f"UPDATE nhacungcap SET {set_clause} WHERE MaNhaCungCap = %s"
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, tuple(values))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def deleteSupplier(supplier_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM nhacungcap WHERE MaNhaCungCap = %s', (supplier_id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
