import os
from dotenv import load_dotenv
from mysql.connector import pooling, Error

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASS", ""),
    "database": os.getenv("DB_NAME", "qlbh"),
    "port": int(os.getenv("DB_PORT", 3306)),
}

pool = None

def init_db_pool(pool_name="mypool", pool_size=5):
    global pool
    if pool is None:
        pool = pooling.MySQLConnectionPool(pool_name=pool_name, pool_size=pool_size, **DB_CONFIG)

def get_connection():
    if pool is None:
        init_db_pool()
    return pool.get_connection()

def test_connection():
    try:
        conn = get_connection()
        conn.close()
        print("✅ Kết nối Database thành công")
    except Error as e:
        print("❌ Kết nối Database thất bại:", e)
