from ..config.connectDB import get_connection

def getAllProducts():
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
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def getAllCategories():
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM loaisanpham')
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def getProductById(product_id):
  conn = get_connection()
  try:
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM sanpham WHERE MaSanPham = %s', (product_id,))
    return cursor.fetchone()
  finally:
    cursor.close()
    conn.close()

def createProduct(data: dict):
  conn = get_connection()
  try:
    cursor = conn.cursor()
    query = '''
    INSERT INTO sanpham (MaSanPham, TenSanPham, MaLoaiSanPham, SoLuongTon, DonGiaBanRa, HinhAnh, isDelete)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    values = (
      data.get('MaSanPham'),
      data.get('TenSanPham'),
      data.get('MaLoaiSanPham'),
      data.get('SoLuongTon', 0),
      data.get('DonGiaBanRa', 0),
      data.get('HinhAnh', ''),
      data.get('isDelete', 1),
    )
    cursor.execute(query, values)
    conn.commit()
    return cursor.lastrowid
  finally:
    cursor.close()
    conn.close()

def updateProduct(product_id, data: dict):
  conn = get_connection()
  try:
    cursor = conn.cursor()
    query = '''
    UPDATE sanpham
    SET TenSanPham = %s, MaLoaiSanPham = %s, HinhAnh = %s, DonGiaBanRa = %s, SoLuongTon = %s, isDelete = %s
    WHERE MaSanPham = %s
    '''
    values = (
      data.get('TenSanPham'),
      data.get('MaLoaiSanPham'),
      data.get('HinhAnh'),
      data.get('DonGiaBanRa', 0),
      data.get('SoLuongTon', 0),
      data.get('isDelete', 1),
      product_id,
    )
    cursor.execute(query, values)
    conn.commit()
    return cursor.rowcount
  finally:
    cursor.close()
    conn.close()

def deleteProduct(product_id):
  conn = get_connection()
  try:
    cursor = conn.cursor()
    cursor.execute('DELETE FROM sanpham WHERE MaSanPham = %s', (product_id,))
    conn.commit()
    return cursor.rowcount
  finally:
    cursor.close()
    conn.close()


def activateProduct(product_id):
  conn = get_connection()
  try:
    cursor = conn.cursor()
    cursor.execute('UPDATE sanpham SET isDelete = 0 WHERE MaSanPham = %s', (product_id,))
    conn.commit()
    return cursor.rowcount
  finally:
    cursor.close()
    conn.close()


def deleteProducts(product_ids):
  if not product_ids:
    return 0

  conn = get_connection()
  try:
    cursor = conn.cursor()
    total = 0
    for product_id in product_ids:
      cursor.execute('SELECT isDelete FROM sanpham WHERE MaSanPham = %s', (product_id,))
      row = cursor.fetchone()
      if not row:
        continue
      is_deleted = row[0]
      if is_deleted:
        cursor.execute('DELETE FROM sanpham WHERE MaSanPham = %s', (product_id,))
      else:
        cursor.execute('UPDATE sanpham SET isDelete = 1 WHERE MaSanPham = %s', (product_id,))
      total += cursor.rowcount
    conn.commit()
    return total
  finally:
    cursor.close()
    conn.close()
