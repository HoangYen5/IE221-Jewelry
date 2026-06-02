from ..config.connectDB import get_connection

def getDashboardStats():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        stats = {}

        # Total revenue from sales
        cursor.execute('SELECT COALESCE(SUM(TongTien), 0) AS total FROM PHIEUBANHANG')
        stats['revenue'] = cursor.fetchone()['total']

        # Total customers
        cursor.execute('SELECT COUNT(*) AS total FROM KHACHHANG')
        stats['customers'] = cursor.fetchone()['total']

        # Total sales orders
        cursor.execute('SELECT COUNT(*) AS total FROM PHIEUBANHANG')
        stats['orders'] = cursor.fetchone()['total']

        # Total products
        cursor.execute('SELECT COUNT(*) AS total FROM SANPHAM WHERE isDelete = 0')
        stats['products'] = cursor.fetchone()['total']

        return stats
    finally:
        cursor.close()
        conn.close()

def getRevenue():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
            SELECT MONTH(NgayLap) AS month, YEAR(NgayLap) AS year,
                   SUM(TongTien) AS total
            FROM PHIEUBANHANG
            GROUP BY YEAR(NgayLap), MONTH(NgayLap)
            ORDER BY year, month
        ''')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def getCategory():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
            SELECT l.TenLoaiSanPham, COUNT(s.MaSanPham) AS SoLuong
            FROM LOAISANPHAM l
            LEFT JOIN SANPHAM s ON l.MaLoaiSanPham = s.MaLoaiSanPham
            GROUP BY l.MaLoaiSanPham, l.TenLoaiSanPham
        ''')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def getOrder():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('''
            SELECT p.SoPhieuBH, p.NgayLap, p.TongTien, k.TenKH
            FROM PHIEUBANHANG p
            LEFT JOIN KHACHHANG k ON p.MaKH = k.MaKH
            ORDER BY p.NgayLap DESC
            LIMIT 10
        ''')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()