from . import __name__
from ..db import get_connection

def get_all_products():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        query = '''
        SELECT 
          s.MaSanPham,
          s.TenSanPham,
          s.HinhAnh,
          s.MaLoaiSanPham,
          s.isDelete,
          s.DonGiaMuaVao,
          (
            COALESCE((SELECT SUM(SoLuongMua) FROM chitietmuahang WHERE MaSanPham = s.MaSanPham), 0) - 
            COALESCE((SELECT SUM(SoLuongBan) FROM chitietbanhang WHERE MaSanPham = s.MaSanPham), 0)
          ) AS SoLuongTon,
          CASE 
            WHEN s.DonGiaMuaVao > 0 THEN 
               ROUND(s.DonGiaMuaVao * (1 + (COALESCE(l.PhanTramLoiNhuan, 0) / 100)))
            ELSE s.DonGiaBanRa 
          END AS DonGiaBanRa,
          l.TenLoaiSanPham,
          l.PhanTramLoiNhuan

        FROM sanpham s 
        LEFT JOIN loaisanpham l ON s.MaLoaiSanPham = l.MaLoaiSanPham
        ORDER BY s.MaSanPham DESC
        '''
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    finally:
        cursor.close()
        conn.close()

def get_all_categories():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM loaisanpham")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def get_products_by_ids(ids):
    if not ids:
        return []
    placeholders = ','.join(['%s'] * len(ids))
    query = f"SELECT MaSanPham, isDelete, HinhAnh FROM sanpham WHERE MaSanPham IN ({placeholders})"
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, ids)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def status_change(ids):
    if not ids:
        return None
    placeholders = ','.join(['%s'] * len(ids))
    query = f"UPDATE sanpham SET isDelete = 1 WHERE MaSanPham IN ({placeholders})"
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, ids)
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def delete_product(ids):
    if not ids:
        return None
    placeholders = ','.join(['%s'] * len(ids))
    query = f"DELETE FROM sanpham WHERE MaSanPham IN ({placeholders})"
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, ids)
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def active_product(id_):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE sanpham SET isDelete = 0 WHERE MaSanPham = %s", (id_,))
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()

def create_product(data: dict):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = '''
        INSERT INTO sanpham (MaSanPham, TenSanPham, MaLoaiSanPham, SoLuongTon, DonGiaBanRa, HinhAnh, isDelete)
        VALUES (%s, %s, %s, 0, 0, %s, 1)
        '''
        values = (data.get('MaSanPham'), data.get('TenSanPham'), data.get('MaLoaiSanPham'), data.get('HinhAnh') or "")
        cursor.execute(query, values)
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        conn.close()

def update_product(data: dict):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = '''
        UPDATE sanpham 
        SET TenSanPham = %s, MaLoaiSanPham = %s, HinhAnh = %s
        WHERE MaSanPham = %s
        '''
        values = (data.get('TenSanPham'), data.get('MaLoaiSanPham'), data.get('HinhAnh'), data.get('MaSanPham'))
        cursor.execute(query, values)
        conn.commit()
        return cursor.rowcount
    finally:
        cursor.close()
        conn.close()
