#!/usr/bin/env python
"""
Complete setup script for Employee Management API
Run this once to set up everything
"""

import subprocess
import sys
import os

def run_command(command):
    """Run a shell command and print output"""
    print(f"\n📦 Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ Command successful")
        if result.stdout:
            print(result.stdout)
        return True
    else:
        print("❌ Command failed")
        if result.stderr:
            print(result.stderr)
        return False

def main():
    print("=" * 60)
    print("Employee Management API - Complete Setup")
    print("=" * 60)
    
    # Step 1: Check if venv exists
    print("\n1️⃣ Checking virtual environment...")
    if not os.path.exists("venv"):
        print("Creating virtual environment...")
        run_command("python -m venv venv")
    
    # Step 2: Activate venv and install packages
    print("\n2️⃣ Installing required packages...")
    if sys.platform == "win32":
        activate_cmd = "venv\\Scripts\\activate && "
    else:
        activate_cmd = "source venv/bin/activate && "
    
    packages = [
        "fastapi", "uvicorn", "sqlalchemy", "pydantic", 
        "python-multipart", "pymysql", "cryptography"
    ]
    
    for package in packages:
        run_command(f"{activate_cmd}python -m pip install {package}")
    
    # Step 3: Create database
    print("\n3️⃣ Setting up MySQL database...")
    try:
        import pymysql
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            charset='utf8mb4'
        )
        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS employee_management")
            print("✅ Database 'employee_management' created or already exists")
        connection.close()
    except Exception as e:
        print(f"⚠️ Could not connect to MySQL: {e}")
        print("Please make sure XAMPP MySQL is running")
    
    # Step 4: Create tables
    print("\n4️⃣ Creating database tables...")
    run_command(f"{activate_cmd}python -c \"from app.database import engine, Base; from app import models; Base.metadata.create_all(bind=engine); print('Tables created successfully')\"")
    
    # Step 5: Test connection
    print("\n5️⃣ Testing database connection...")
    run_command(f"{activate_cmd}python -c \"from app.database import engine; from sqlalchemy import text; conn = engine.connect(); result = conn.execute(text('SELECT 1')); print('✅ Database connection successful')\"")
    
    print("\n" + "=" * 60)
    print("✅ Setup Complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Make sure XAMPP MySQL is running")
    print("2. Run: python run.py")
    print("3. Open browser to: http://localhost:8000/docs")
    print("\nOr use VS Code debugger:")
    print("- Press F5")
    print("- Select 'FastAPI Application'")

if __name__ == "__main__":
    main()