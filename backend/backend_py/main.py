import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

from .db import init_db_pool, test_connection

app = FastAPI(title="JewelryStore API (Python)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from .routes import product_route

app.include_router(product_route.router)


@app.on_event("startup")
def startup_event():
    init_db_pool()
    test_connection()

@app.get("/")
def root():
    return {"message": "Server đang chạy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend_py.main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8080)), reload=True)
