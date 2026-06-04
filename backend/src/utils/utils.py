def generate_id(cursor, table: str, column: str, prefix: str) -> str:
    query = f"SELECT {column} FROM {table} WHERE {column} LIKE %s ORDER BY LENGTH({column}) DESC, {column} DESC LIMIT 1"
    cursor.execute(query, (f"{prefix}%",))
    row = cursor.fetchone()
    
    # Try fetching as tuple or dict depending on cursor type
    last_id = None
    if row:
        if isinstance(row, dict):
            last_id = row.get(column)
        else:
            last_id = row[0]

    if last_id and last_id.startswith(prefix):
        num_str = last_id[len(prefix):]
        if num_str.isdigit():
            next_num = int(num_str) + 1
            padding = len(num_str)
            # Ensure padding is at least 2 digits to match SP01 format
            padding = max(padding, 2)
            return f"{prefix}{str(next_num).zfill(padding)}"
            
    return f"{prefix}01"
