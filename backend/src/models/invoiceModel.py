from ..config.connectDB import get_connection

def getAllInvoices():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
            SELECT p.*, k.TenKH
            FROM PHIEUBANHANG p
            LEFT JOIN KHACHHANG k ON p.MaKH = k.MaKH
            ORDER BY p.NgayLap DESC
        ''')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def getInvoiceById(invoice_id):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
            SELECT p.*, k.TenKH
            FROM PHIEUBANHANG p
            LEFT JOIN KHACHHANG k ON p.MaKH = k.MaKH
            WHERE p.SoPhieuBH = %s
        ''', (invoice_id,))
        invoice = cursor.fetchone()
        if invoice:
            cursor.execute('''
                SELECT ct.*, sp.TenSanPham
                FROM CHITIETBANHANG ct
                LEFT JOIN SANPHAM sp ON ct.MaSanPham = sp.MaSanPham
                WHERE ct.SoPhieuBH = %s
            ''', (invoice_id,))
            invoice['details'] = cursor.fetchall()
        return invoice
    finally:
        cursor.close()
        conn.close()

def createInvoice(data: dict):
    if not data:
        return None
    conn = get_connection()
    try:
        cursor = conn.cursor()
        # Insert invoice header
        cursor.execute('''
            INSERT INTO PHIEUBANHANG (SoPhieuBH, NgayLap, MaKH, TongTien)
            VALUES (%s, %s, %s, %s)
        ''', (
            data.get('SoPhieuBH'),
            data.get('NgayLap'),
            data.get('MaKH'),
            data.get('TongTien', 0),
        ))
        # Insert invoice details
        details = data.get('details', [])
        for i, d in enumerate(details):
            detail_id = f"CTBH_{data.get('SoPhieuBH')}_{i+1}"
            cursor.execute('''
                INSERT INTO CHITIETBANHANG (MaChiTietBH, SoPhieuBH, MaSanPham, SoLuongBan, DonGiaBan, ThanhTien)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (
                detail_id,
                data.get('SoPhieuBH'),
                d.get('MaSanPham'),
                d.get('SoLuongBan'),
                d.get('DonGiaBan'),
                d.get('ThanhTien', 0),
            ))
        conn.commit()
        return data.get('SoPhieuBH')
    finally:
        cursor.close()
        conn.close()

def updateInvoice(invoice_id, data: dict):
    if not data:
        return 0
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sets = []
        vals = []
        for k, v in data.items():
            if k not in ('SoPhieuBH', 'details'):
                sets.append(f"{k} = %s")
                vals.append(v)
        if sets:
            vals.append(invoice_id)
            query = f"UPDATE PHIEUBANHANG SET {','.join(sets)} WHERE SoPhieuBH = %s"
            cursor.execute(query, tuple(vals))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def deleteInvoice(invoice_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM PHIEUBANHANG WHERE SoPhieuBH = %s', (invoice_id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def deleteInvoices(invoice_ids):
    if not invoice_ids:
        return 0
    conn = get_connection()
    try:
        cursor = conn.cursor()
        total = 0
        for iid in invoice_ids:
            cursor.execute('DELETE FROM PHIEUBANHANG WHERE SoPhieuBH = %s', (iid,))
            total += cursor.rowcount
        conn.commit()
        return total
    finally:
        cursor.close()
        conn.close()
