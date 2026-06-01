from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_NAME = os.getenv("DB_NAME", "qlbh")
DB_PORT = os.getenv("DB_PORT", "3306")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

def test_connection():
    try:
        conn = engine.connect()
        conn.close()
        print('✅ Đã kết nối MySQL qua SQLAlchemy thành công!')
    except Exception as e:
        print('❌ Không thể kết nối SQL:', e)
