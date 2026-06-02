from ..config.connectDB import get_connection

def getAllEmployees():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT MaTaiKhoan, TenTaiKhoan, Role, createdAt FROM TAIKHOAN ORDER BY MaTaiKhoan')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def getEmployeeById(employee_id):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT MaTaiKhoan, TenTaiKhoan, Role, createdAt FROM TAIKHOAN WHERE MaTaiKhoan = %s', (employee_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def createEmployee(data: dict):
    if not data:
        return None
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO TAIKHOAN (TenTaiKhoan, MatKhau, Role)
            VALUES (%s, %s, %s)
        ''', (
            data.get('TenTaiKhoan'),
            data.get('MatKhau'),
            data.get('Role', 'seller'),
        ))
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        conn.close()

def updateEmployee(employee_id, data: dict):
    if not data:
        return 0
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sets = []
        vals = []
        for k, v in data.items():
            if k != 'MaTaiKhoan':
                sets.append(f"{k} = %s")
                vals.append(v)
        if not sets:
            return 0
        vals.append(employee_id)
        query = f"UPDATE TAIKHOAN SET {','.join(sets)} WHERE MaTaiKhoan = %s"
        cursor.execute(query, tuple(vals))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def deleteEmployee(employee_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM TAIKHOAN WHERE MaTaiKhoan = %s', (employee_id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
