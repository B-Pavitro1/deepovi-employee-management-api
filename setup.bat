@echo off
title Employee Management API - Setup & Run
color 0A

echo ========================================
echo Employee Management API - Setup & Run
echo ========================================
echo.

REM Navigate to project directory
cd /d D:\employee-management-api

REM Check if XAMPP MySQL is running
echo Checking MySQL connection...
python -c "import pymysql; pymysql.connect(host='localhost', user='root', password='')" 2>nul
if errorlevel 1 (
    echo [WARNING] MySQL is not running!
    echo Please start MySQL in XAMPP Control Panel
    echo.
    pause
    exit /b 1
)
echo [OK] MySQL is running
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
echo [OK] Virtual environment activated
echo.

REM Install/Update requirements
echo Installing/Updating requirements...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo [OK] Requirements installed
echo.

REM Setup database
echo Setting up database...
python -c "from app.database import engine, Base; from app import models; Base.metadata.create_all(bind=engine)"
echo [OK] Database tables created
echo.

REM Ask about sample data
set /p add_data="Do you want to add sample data? (y/n): "
if /i "%add_data%"=="y" (
    echo Adding sample data...
    python add_sample_data.py
    echo [OK] Sample data added
    echo.
)

REM Run the application
echo ========================================
echo Starting Employee Management API...
echo ========================================
echo.
echo API will be available at: http://localhost:8000
echo Documentation at: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.

python run.py

pause