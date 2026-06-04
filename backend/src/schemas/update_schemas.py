import glob
import re
import os

schema_dir = '/home/hnim3107/Data/Projects/IE221-Jewelry/backend/src/schemas/'
files = glob.glob(schema_dir + '*.py')

target_fields = [
    'MaSanPham', 'MaKH', 'MaNCC', 'MaDVT', 'MaLoaiSanPham', 'MaLoaiDV'
]

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    modified = False
    
    # We only want to replace it if it's the primary key being created, but replacing all is safer for testing.
    for field in target_fields:
        pattern = rf'^(\s+){field}:\s*str(\s*)$'
        # We need multiline replacement
        lines = content.split('\n')
        for i, line in enumerate(lines):
            match = re.match(pattern, line)
            if match:
                lines[i] = f"{match.group(1)}{field}: Optional[str] = None"
                modified = True
        if modified:
            content = '\n'.join(lines)
            
    if modified:
        if 'Optional' not in content:
            if 'from typing import' in content:
                content = content.replace('from typing import', 'from typing import Optional,')
            else:
                content = 'from typing import Optional\n' + content
        with open(f, 'w') as file:
            file.write(content)

print("Updated schemas.")
