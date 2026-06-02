from ..config.connectDB import get_connection

def getAllServiceTickets():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
            SELECT p.*, k.TenKH
            FROM PHIEUDICHVU p
            LEFT JOIN KHACHHANG k ON p.MaKH = k.MaKH
            ORDER BY p.NgayLap DESC
        ''')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def getServiceTicketById(ticket_id):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
            SELECT p.*, k.TenKH
            FROM PHIEUDICHVU p
            LEFT JOIN KHACHHANG k ON p.MaKH = k.MaKH
            WHERE p.SoPhieuDV = %s
        ''', (ticket_id,))
        ticket = cursor.fetchone()
        if ticket:
            cursor.execute('''
                SELECT ct.*, l.TenLoaiDV
                FROM CHITIETPHIEUDICHVU ct
                LEFT JOIN LOAIDICHVU l ON ct.MaLoaiDV = l.MaLoaiDV
                WHERE ct.SoPhieuDV = %s
            ''', (ticket_id,))
            ticket['details'] = cursor.fetchall()
        return ticket
    finally:
        cursor.close()
        conn.close()

def createServiceTicket(data: dict):
    if not data:
        return None
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO PHIEUDICHVU (SoPhieuDV, NgayLap, MaKH, TongTien, TongTienTraTruoc, TongTienConLai, TinhTrang)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (
            data.get('SoPhieuDV'),
            data.get('NgayLap'),
            data.get('MaKH'),
            data.get('TongTien', 0),
            data.get('TongTienTraTruoc', 0),
            data.get('TongTienConLai', 0),
            data.get('TinhTrang', 'Đang xử lý'),
        ))
        details = data.get('details', [])
        for i, d in enumerate(details):
            detail_id = f"CTDV_{data.get('SoPhieuDV')}_{i+1}"
            cursor.execute('''
                INSERT INTO CHITIETPHIEUDICHVU (MaChiTietDV, SoPhieuDV, MaLoaiDV, DonGiaDuocTinh, SoLuong, ThanhTien, TraTruoc, ConLai, NgayGiao, TinhTrang)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                detail_id,
                data.get('SoPhieuDV'),
                d.get('MaLoaiDV'),
                d.get('DonGiaDuocTinh'),
                d.get('SoLuong', 1),
                d.get('ThanhTien', 0),
                d.get('TraTruoc', 0),
                d.get('ConLai', 0),
                d.get('NgayGiao'),
                d.get('TinhTrang', 'Chưa hoàn thành'),
            ))
        conn.commit()
        return data.get('SoPhieuDV')
    finally:
        cursor.close()
        conn.close()

def updateServiceTicketStatus(ticket_id, status):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('UPDATE PHIEUDICHVU SET TinhTrang = %s WHERE SoPhieuDV = %s', (status, ticket_id))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def deleteServiceTicket(ticket_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM PHIEUDICHVU WHERE SoPhieuDV = %s', (ticket_id,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def deleteServiceTickets(ticket_ids):
    if not ticket_ids:
        return 0
    conn = get_connection()
    try:
        cursor = conn.cursor()
        total = 0
        for tid in ticket_ids:
            cursor.execute('DELETE FROM PHIEUDICHVU WHERE SoPhieuDV = %s', (tid,))
            total += cursor.rowcount
        conn.commit()
        return total
    finally:
        cursor.close()
        conn.close()
