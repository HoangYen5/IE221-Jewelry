from ..config.connectDB import get_connection

def getAllEmployees():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM nhanvien')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def getEmployeeById(employee_id):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM nhanvien WHERE MaNhanVien = %s', (employee_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def createEmployee(data: dict):
    if not data:
        return None
    cols = ','.join(data.keys())
    placeholders = ','.join(['%s'] * len(data))
    values = tuple(data.values())
    query = f"INSERT INTO nhanvien ({cols}) VALUES ({placeholders})"
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, values)
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        conn.close()

def updateEmployee(employee_id, data: dict):
    if not data:
        return 0
    set_clause = ','.join([f"{k} = %s" for k in data.keys()])
    values = list(data.values()) + [employee_id]
    query = f"UPDATE nhanvien SET {set_clause} WHERE MaNhanVien = %s"
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, tuple(values))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def deleteEmployee(employee_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM nhanvien WHERE MaNhanVien = %s', (employee_id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
