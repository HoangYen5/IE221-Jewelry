<#
Setup Python virtual environment and install backend dependencies.
Usage: Open PowerShell in this folder and run: .\setup_env.ps1
This script expects `python` available on PATH (Python 3.8+ recommended).
#>
Write-Host "Running backend environment setup..."

$Root = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $Root

# Check python
try {
    $py = & python -V 2>&1
} catch {
    Write-Error "Python not found. Install Python 3 and add to PATH."
    exit 1
}

Write-Host "Found Python: $py"

# Create venv
if (-not (Test-Path -Path .venv)) {
    Write-Host "Creating virtual environment..."
    & python -m venv .venv
} else {
    Write-Host ".venv already exists, skipping venv creation."
}

Write-Host "Bootstrapping pip (ensurepip) and upgrading pip..."
# Ensure pip exists inside venv
& .venv\Scripts\python.exe -m ensurepip --upgrade 2>$null
& .venv\Scripts\python.exe -m pip install --upgrade pip

if (Test-Path requirements.txt) {
    & .venv\Scripts\python.exe -m pip install -r requirements.txt
} else {
    Write-Error "requirements.txt not found in backend folder."
    exit 1
}

# Copy .env.example to .env if missing
if ((Test-Path .env.example) -and -not (Test-Path .env)) {
    Copy-Item .env.example .env
    Write-Host "Copied .env.example -> .env (remember to edit DB credentials)."
} elseif (-not (Test-Path .env.example)) {
    Write-Warning ".env.example not found; create .env manually." 
} else {
    Write-Host ".env already exists, leaving untouched."
}

Write-Host "Setup complete. To run the server: .\run_backend.ps1"
exit 0
