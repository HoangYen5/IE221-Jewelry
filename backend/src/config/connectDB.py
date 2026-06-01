import os
from dotenv import load_dotenv
from mysql.connector import pooling, Error

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASS", ""),
    "database": os.getenv("DB_NAME", "qlbh"),
    "port": int(os.getenv("DB_PORT", 3306)),
}

pool = None

def connectDB(pool_name="app_pool", pool_size=5):
    global pool
    if pool is None:
        try:
            pool = pooling.MySQLConnectionPool(pool_name=pool_name, pool_size=pool_size, **DB_CONFIG)
            print("Kết nối Database qlbh thành công!")
        except Error as e:
            print("Kết nối thất bại:", e)

def get_connection():
    if pool is None:
        connectDB()
    return pool.get_connection()
