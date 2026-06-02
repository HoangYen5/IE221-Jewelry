import os
import re

ROUTES_DIR = "/home/hnim3107/Data/Projects/IE221-Jewelry/backend/src/routes"

routes = [
    "dashboardRoute", "productTypeRoute", "serviceTicketRoute",
    "unitRoute", "serviceTypeRoute", "invoiceRoute", "purchaseRoute",
    "supplierRoute", "reportRoute", "profileRoute", "employeeRoute",
    "categoryRoute"
]

for route in routes:
    route_file = os.path.join(ROUTES_DIR, f"{route}.py")
    if not os.path.exists(route_file):
        continue
        
    with open(route_file, "r") as f:
        content = f.read()
        
    # Replace (payload) with (payload.model_dump())
    content = re.sub(r'\(payload\)', '(payload.model_dump())', content)
    # Replace (id, payload) with (id, payload.model_dump(exclude_unset=True))
    # We can match `([a-zA-Z_]+, payload)`
    content = re.sub(r'\(([a-zA-Z_]+),\s*payload\)', r'(\1, payload.model_dump(exclude_unset=True))', content)
    
    with open(route_file, "w") as f:
        f.write(content)

print("Fixed payload.model_dump()")
