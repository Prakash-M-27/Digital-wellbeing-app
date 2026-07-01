@echo off
echo ========================================
echo Digital Well-Being Bot - Quick Start
echo ========================================
echo.

echo [1/3] Installing dependencies...
pip install -r requirements.txt
echo.

echo [2/3] Starting Flask server...
echo.
echo Open your browser and go to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py
