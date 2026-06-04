from ..config.connectDB import get_connection
from ..utils.utils import generate_id

def getAllProductTypes():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
            SELECT l.*, d.TenDVT
            FROM LOAISANPHAM l
            LEFT JOIN DONVITINH d ON l.MaDVT = d.MaDVT
        ''')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def createProductType(data: dict):
    if not data:
        return None
    conn = get_connection()
    try:
        cursor = conn.cursor()
        
        ma_lsp = data.get('MaLoaiSanPham')
        if not ma_lsp:
            ma_lsp = generate_id(cursor, 'LOAISANPHAM', 'MaLoaiSanPham', 'LSP')
            
        cursor.execute('''
            INSERT INTO LOAISANPHAM (MaLoaiSanPham, TenLoaiSanPham, MaDVT, PhanTramLoiNhuan)
            VALUES (%s, %s, %s, %s)
        ''', (
            ma_lsp,
            data.get('TenLoaiSanPham'),
            data.get('MaDVT'),
            data.get('PhanTramLoiNhuan', 30),
        ))
        conn.commit()
        return ma_lsp
    finally:
        cursor.close()
        conn.close()

def updateProductType(type_id, data: dict):
    if not data:
        return 0
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sets = []
        vals = []
        for k, v in data.items():
            if k != 'MaLoaiSanPham':
                sets.append(f"{k} = %s")
                vals.append(v)
        if not sets:
            return 0
        vals.append(type_id)
        query = f"UPDATE LOAISANPHAM SET {','.join(sets)} WHERE MaLoaiSanPham = %s"
        cursor.execute(query, tuple(vals))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def deleteProductType(type_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM LOAISANPHAM WHERE MaLoaiSanPham = %s', (type_id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
