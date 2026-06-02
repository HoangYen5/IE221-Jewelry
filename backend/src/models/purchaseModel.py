from ..config.connectDB import get_connection

def getAllPurchases():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
            SELECT p.*, n.TenNCC
            FROM PHIEUMUAHANG p
            LEFT JOIN NHACUNGCAP n ON p.MaNCC = n.MaNCC
            ORDER BY p.NgayLap DESC
        ''')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def getPurchaseById(purchase_id):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
            SELECT p.*, n.TenNCC
            FROM PHIEUMUAHANG p
            LEFT JOIN NHACUNGCAP n ON p.MaNCC = n.MaNCC
            WHERE p.SoPhieuMH = %s
        ''', (purchase_id,))
        purchase = cursor.fetchone()
        if purchase:
            cursor.execute('''
                SELECT ct.*, sp.TenSanPham
                FROM CHITIETMUAHANG ct
                LEFT JOIN SANPHAM sp ON ct.MaSanPham = sp.MaSanPham
                WHERE ct.SoPhieuMH = %s
            ''', (purchase_id,))
            purchase['details'] = cursor.fetchall()
        return purchase
    finally:
        cursor.close()
        conn.close()

def createPurchase(data: dict):
    if not data:
        return None
    conn = get_connection()
    try:
        cursor = conn.cursor()
        # Insert purchase header
        cursor.execute('''
            INSERT INTO PHIEUMUAHANG (SoPhieuMH, NgayLap, MaNCC, TongTien)
            VALUES (%s, %s, %s, %s)
        ''', (
            data.get('SoPhieuMH'),
            data.get('NgayLap'),
            data.get('MaNCC'),
            data.get('TongTien', 0),
        ))
        # Insert purchase details
        details = data.get('details', [])
        for i, d in enumerate(details):
            detail_id = f"CTMH_{data.get('SoPhieuMH')}_{i+1}"
            cursor.execute('''
                INSERT INTO CHITIETMUAHANG (MaChiTietMH, SoPhieuMH, MaSanPham, SoLuongMua, DonGiaMua, ThanhTien)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (
                detail_id,
                data.get('SoPhieuMH'),
                d.get('MaSanPham'),
                d.get('SoLuongMua'),
                d.get('DonGiaMua'),
                d.get('ThanhTien', 0),
            ))
            # Update product purchase price
            cursor.execute('''
                UPDATE SANPHAM SET DonGiaMuaVao = %s WHERE MaSanPham = %s
            ''', (d.get('DonGiaMua'), d.get('MaSanPham')))
        conn.commit()
        return data.get('SoPhieuMH')
    finally:
        cursor.close()
        conn.close()

def updatePurchase(purchase_id, data: dict):
    if not data:
        return 0
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sets = []
        vals = []
        for k, v in data.items():
            if k not in ('SoPhieuMH', 'details'):
                sets.append(f"{k} = %s")
                vals.append(v)
        if sets:
            vals.append(purchase_id)
            query = f"UPDATE PHIEUMUAHANG SET {','.join(sets)} WHERE SoPhieuMH = %s"
            cursor.execute(query, tuple(vals))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def deletePurchase(purchase_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM PHIEUMUAHANG WHERE SoPhieuMH = %s', (purchase_id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def deletePurchases(purchase_ids):
    if not purchase_ids:
        return 0
    conn = get_connection()
    try:
        cursor = conn.cursor()
        total = 0
        for pid in purchase_ids:
            cursor.execute('DELETE FROM PHIEUMUAHANG WHERE SoPhieuMH = %s', (pid,))
            total += cursor.rowcount
        conn.commit()
        return total
    finally:
        cursor.close()
        conn.close()
