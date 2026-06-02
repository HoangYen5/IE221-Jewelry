import os
import re

ROUTES_DIR = "/home/hnim3107/Data/Projects/IE221-Jewelry/backend/src/routes"
SCHEMAS_DIR = "/home/hnim3107/Data/Projects/IE221-Jewelry/backend/src/schemas"

os.makedirs(SCHEMAS_DIR, exist_ok=True)

routes = [
    "dashboardRoute", "productTypeRoute", "serviceTicketRoute",
    "unitRoute", "serviceTypeRoute", "invoiceRoute", "purchaseRoute",
    "supplierRoute", "reportRoute", "profileRoute", "employeeRoute",
    "categoryRoute"
]

for route in routes:
    # Create schema file
    entity = route.replace('Route', '')
    schema_name = entity.capitalize() + "Schema"
    schema_file = os.path.join(SCHEMAS_DIR, f"{entity}Schema.py")
    
    with open(schema_file, "w") as f:
        f.write(f'''from pydantic import BaseModel, ConfigDict
from typing import Optional, Any, Dict

class {entity.capitalize()}Base(BaseModel):
    model_config = ConfigDict(extra='allow')

class {entity.capitalize()}Create({entity.capitalize()}Base):
    pass

class {entity.capitalize()}Update({entity.capitalize()}Base):
    pass

class {entity.capitalize()}Response({entity.capitalize()}Base):
    pass
''')
    
    # Update route file
    route_file = os.path.join(ROUTES_DIR, f"{route}.py")
    if not os.path.exists(route_file):
        continue
        
    with open(route_file, "r") as f:
        content = f.read()
        
    # Add imports
    import_statement = f"from ..schemas.{entity}Schema import {entity.capitalize()}Create, {entity.capitalize()}Update, {entity.capitalize()}Response\nfrom typing import Dict, Any, List\n"
    if "from ..schemas" not in content:
        content = content.replace("from fastapi import", import_statement + "from fastapi import")
        
    # Update dict -> Create / Update based on method
    # Rough replacement for simple cases
    content = re.sub(r'def create_[a-zA-Z_]+\(.*?(payload:\s*dict|data:\s*dict).*?\):', lambda m: m.group(0).replace('dict', f'{entity.capitalize()}Create'), content)
    content = re.sub(r'def update_[a-zA-Z_]+\(.*?(payload:\s*dict|data:\s*dict).*?\):', lambda m: m.group(0).replace('dict', f'{entity.capitalize()}Update'), content)
    
    # We'll just replace 'payload: dict' with generic BaseModel for others if they exist
    # But for now, just replacing generic dict payloads
    content = content.replace('payload: dict', f'payload: {entity.capitalize()}Create')
    
    with open(route_file, "w") as f:
        f.write(content)

print("Done generating schemas and refactoring routes!")
