Backend local run helper

1) Create virtualenv and install dependencies:

```powershell
cd backend
.\setup_env.ps1
```

2) Run the backend:

```powershell
cd backend
.\run_backend.ps1
```

Notes:
- Make sure Python 3 is installed and available as `python` in your PATH.
- Edit `.env` in the `backend` folder to set your DB credentials and `JWT_SECRET`.
