from ..config.connectDB import get_connection

def getAllUnits():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM DONVITINH ORDER BY MaDVT')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def getUnitById(unit_id):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM DONVITINH WHERE MaDVT = %s', (unit_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def searchUnits(keyword):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM DONVITINH WHERE TenDVT LIKE %s OR MaDVT LIKE %s',
                       (f'%{keyword}%', f'%{keyword}%'))
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def getNextCode():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT MaDVT FROM DONVITINH ORDER BY MaDVT DESC LIMIT 1")
        row = cursor.fetchone()
        if row:
            last_code = row['MaDVT']
            # Extract number from code like "DVT10" -> 10
            num = int(''.join(filter(str.isdigit, last_code)) or '0') + 1
            return f"DVT{num:02d}"
        return "DVT01"
    finally:
        cursor.close()
        conn.close()

def createUnit(data: dict):
    if not data:
        return None
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO DONVITINH (MaDVT, TenDVT)
            VALUES (%s, %s)
        ''', (data.get('MaDVT'), data.get('TenDVT')))
        conn.commit()
        return data.get('MaDVT')
    finally:
        cursor.close()
        conn.close()

def updateUnit(unit_id, data: dict):
    if not data:
        return 0
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sets = []
        vals = []
        for k, v in data.items():
            if k != 'MaDVT':
                sets.append(f"{k} = %s")
                vals.append(v)
        if not sets:
            return 0
        vals.append(unit_id)
        query = f"UPDATE DONVITINH SET {','.join(sets)} WHERE MaDVT = %s"
        cursor.execute(query, tuple(vals))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def deleteUnit(unit_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM DONVITINH WHERE MaDVT = %s', (unit_id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
