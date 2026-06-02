import os
import re

SQL_FILE = "/home/hnim3107/Data/Projects/IE221-Jewelry/backend/src/sql/data.sql"
SCHEMAS_DIR = "/home/hnim3107/Data/Projects/IE221-Jewelry/backend/src/schemas"

TABLE_TO_SCHEMA = {
    'DONVITINH': [('unit', 'Unit')],
    'LOAISANPHAM': [('productType', 'Producttype'), ('category', 'Category')],
    'SANPHAM': [('product', 'Product')],
    'KHACHHANG': [('customer', 'Customer')],
    'NHACUNGCAP': [('supplier', 'Supplier')],
    'TAIKHOAN': [('profile', 'Profile'), ('employee', 'Employee')],
    'LOAIDICHVU': [('serviceType', 'Servicetype')],
    'PHIEUMUAHANG': [('purchase', 'Purchase')],
    'PHIEUBANHANG': [('invoice', 'Invoice')],
    'PHIEUDICHVU': [('serviceTicket', 'Serviceticket')],
    'BAOCAOTONKHO': [('report', 'Report')]
}

def sql_type_to_python(sql_type: str) -> str:
    t = sql_type.upper()
    if 'VARCHAR' in t or 'CHAR' in t or 'TEXT' in t or 'ENUM' in t:
        return 'str'
    if 'INT' in t:
        return 'int'
    if 'DECIMAL' in t or 'FLOAT' in t or 'DOUBLE' in t:
        return 'float'
    if 'DATETIME' in t or 'DATE' in t or 'TIMESTAMP' in t:
        return 'datetime'
    if 'BOOL' in t:
        return 'bool'
    return 'str'

def parse_sql():
    tables = {}
    with open(SQL_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Matches CREATE TABLE NAME ( ... )
    table_blocks = re.findall(r'CREATE TABLE (\w+)\s*\((.*?)\);', content, re.IGNORECASE | re.DOTALL)
    for table_name, columns_str in table_blocks:
        fields = []
        lines = columns_str.split('\n')
        for line in lines:
            line = line.strip()
            if not line or line.startswith('--') or line.startswith('CONSTRAINT') or line.startswith('PRIMARY KEY'):
                continue
            
            # Match column name and type
            # Example: MaDVT VARCHAR(50) PRIMARY KEY,
            parts = line.split()
            if len(parts) >= 2:
                col_name = parts[0]
                col_type = parts[1]
                # ignore foreign keys definition inside columns (like FOREIGN KEY)
                if col_name.upper() in ['CONSTRAINT', 'FOREIGN', 'PRIMARY']:
                    continue
                
                py_type = sql_type_to_python(col_type)
                is_optional = 'NOT NULL' not in line.upper() and 'PRIMARY KEY' not in line.upper()
                
                fields.append((col_name, py_type, is_optional))
        
        tables[table_name.upper()] = fields
    
    return tables

def generate_schemas(tables):
    for table_name, schema_mappings in TABLE_TO_SCHEMA.items():
        if table_name not in tables:
            print(f"Table {table_name} not found in SQL.")
            continue
            
        fields = tables[table_name]
        
        for file_prefix, class_prefix in schema_mappings:
            schema_file = os.path.join(SCHEMAS_DIR, f"{file_prefix}Schema.py")
            
            # Construct fields string
            fields_str = ""
            for name, py_type, is_optional in fields:
                if is_optional:
                    fields_str += f"    {name}: Optional[{py_type}] = None\n"
                else:
                    fields_str += f"    {name}: {py_type}\n"
            
            content = f"""from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class {class_prefix}Base(BaseModel):
{fields_str}
class {class_prefix}Create({class_prefix}Base):
    pass

class {class_prefix}Update({class_prefix}Base):
    pass

class {class_prefix}Response({class_prefix}Base):
    pass
"""
            # Preserve special schemas like ProductActionRequest
            if file_prefix == 'product':
                content += """
class ProductActionRequest(BaseModel):
    id: Optional[str] = None
    MaSanPham: Optional[str] = None
    ids: Optional[List[str]] = None
"""
            
            with open(schema_file, "w") as f:
                f.write(content)
            print(f"Generated {schema_file}")

if __name__ == '__main__':
    tables = parse_sql()
    generate_schemas(tables)
