This is a Python FastAPI reimplementation of parts of the original Express backend.

Quick start

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Copy environment variables into a `.env` file (DB_HOST, DB_USER, DB_PASS, DB_NAME, JWT_SECRET).

3. Run the server:

```bash
uvicorn backend_py.main:app --reload --port 8080
```

I converted core files (DB pool, auth middleware, product model, product route). Tell me if you want me to continue converting the remaining controllers/services/routes; I can proceed file-by-file or batch-convert all remaining files.
