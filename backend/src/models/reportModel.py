from ..config.connectDB import get_connection


def getReport(params=None):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        if params and ('month' in params or 'year' in params):
            conditions = []
            values = []
            if 'month' in params:
                conditions.append("b.Thang = %s")
                values.append(params['month'])
            if 'year' in params:
                conditions.append("b.Nam = %s")
                values.append(params['year'])
            where = " AND ".join(conditions)
            cursor.execute(
                f"SELECT b.*, s.TenSanPham FROM BAOCAOTONKHO b LEFT JOIN SANPHAM s ON b.MaSanPham = s.MaSanPham WHERE {where} ORDER BY b.Nam DESC, b.Thang DESC",
                tuple(values)
            )
        else:
            cursor.execute(
                "SELECT b.*, s.TenSanPham FROM BAOCAOTONKHO b LEFT JOIN SANPHAM s ON b.MaSanPham = s.MaSanPham ORDER BY b.Nam DESC, b.Thang DESC"
            )
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()


def getReportById(thang: int, nam: int, ma_san_pham: str):
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT b.*, s.TenSanPham FROM BAOCAOTONKHO b LEFT JOIN SANPHAM s ON b.MaSanPham = s.MaSanPham WHERE b.Thang = %s AND b.Nam = %s AND b.MaSanPham = %s",
            (thang, nam, ma_san_pham)
        )
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()


def createReport(data: dict):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT IGNORE INTO BAOCAOTONKHO (Thang, Nam, MaSanPham, TonDau, SoLuongMuaVao, SoLuongBanRa, TonCuoi)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (
            data.get('Thang'),
            data.get('Nam'),
            data.get('MaSanPham'),
            data.get('TonDau', 0),
            data.get('SoLuongMuaVao', 0),
            data.get('SoLuongBanRa', 0),
            data.get('TonCuoi', 0),
        ))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
