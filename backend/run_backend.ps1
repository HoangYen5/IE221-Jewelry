<#
Run the backend FastAPI server inside the virtualenv.
Usage: from backend folder: .\run_backend.ps1
#>
Write-Host "Starting backend server..."

$Root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $Root

if (-not (Test-Path .venv)) {
    Write-Error ".venv not found. Run .\setup_env.ps1 first to create virtual environment."
    exit 1
}

& .venv\Scripts\python.exe -m uvicorn index:app --reload --port 8080
