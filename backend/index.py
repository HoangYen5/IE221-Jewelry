import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Ensure src is importable
HERE = os.path.dirname(__file__)
# Add backend folder (parent of src) so `import src...` works
if HERE not in sys.path:
    sys.path.insert(0, HERE)

from dotenv import load_dotenv
load_dotenv()

from src.config.connectDB import connectDB

app = FastAPI(title="JewelryStore API (converted)")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
from fastapi.staticfiles import StaticFiles
from src.routes.productRoute import router as product_router
from src.routes.userRoute import router as user_router
from src.routes.dashboardRoute import router as dashboard_router
from src.routes.productTypeRoute import router as product_type_router
from src.routes.serviceTicketRoute import router as service_ticket_router
from src.routes.unitRoute import router as unit_router
from src.routes.serviceTypeRoute import router as service_type_router
from src.routes.invoiceRoute import router as invoice_router
from src.routes.customerRoute import router as customer_router
from src.routes.purchaseRoute import router as purchase_router
from src.routes.supplierRoute import router as supplier_router
from src.routes.reportRoute import router as report_router
from src.routes.profileRoute import router as profile_router
from src.routes.employeeRoute import router as employee_router
from src.routes.categoryRoute import router as category_router

app.include_router(product_router)
app.include_router(user_router)
app.include_router(dashboard_router)
app.include_router(product_type_router)
app.include_router(service_ticket_router)
app.include_router(unit_router)
app.include_router(service_type_router)
app.include_router(invoice_router)
app.include_router(customer_router)
app.include_router(purchase_router)
app.include_router(supplier_router)
app.include_router(report_router)
app.include_router(profile_router)
app.include_router(employee_router)
app.include_router(category_router)

app.mount("/uploads", StaticFiles(directory=os.path.join(HERE, "uploads")), name="uploads")

@app.on_event('startup')
def on_startup():
    connectDB()

@app.get('/')
def root():
    return {'message': 'Server đang chạy (Python)'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('index:app', host='0.0.0.0', port=int(os.getenv('PORT', 8080)), reload=True)
