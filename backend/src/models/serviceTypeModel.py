from ..config.connectDB import get_connection
from ..utils.utils import generate_id

def getAllServiceTypes():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM LOAIDICHVU')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def createServiceType(data: dict):
    if not data:
        return None
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        ma_loai = data.get('MaLoaiDV')
        if not ma_loai:
            ma_loai = generate_id(cursor, 'LOAIDICHVU', 'MaLoaiDV', 'LDV')
            
        cursor.execute('''
            INSERT INTO LOAIDICHVU (MaLoaiDV, TenLoaiDV, DonGiaDV, PhanTramTraTruoc)
            VALUES (%s, %s, %s, %s)
        ''', (
            ma_loai,
            data.get('TenLoaiDV'),
            data.get('DonGiaDV', 0),
            data.get('PhanTramTraTruoc', 0.5),
        ))
        conn.commit()
        return ma_loai
    finally:
        cursor.close()
        conn.close()

def updateServiceType(type_id, data: dict):
    if not data:
        return 0
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sets = []
        vals = []
        for k, v in data.items():
            if k != 'MaLoaiDV':
                sets.append(f"{k} = %s")
                vals.append(v)
        if not sets:
            return 0
        vals.append(type_id)
        query = f"UPDATE LOAIDICHVU SET {','.join(sets)} WHERE MaLoaiDV = %s"
        cursor.execute(query, tuple(vals))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def deleteServiceType(type_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM LOAIDICHVU WHERE MaLoaiDV = %s', (type_id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
