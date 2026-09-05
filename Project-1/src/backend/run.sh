#!/usr/bin/env bash
set -e

echo "===================================================="
echo "Starting OracleDocuAI FastAPI Backend Server"
echo "===================================================="

if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate
pip install -q --upgrade pip
pip install -q -r requirements.txt

echo "Starting server on http://localhost:8000..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
