"""
Add sample employee data to the database
Run this after setup to populate test data
"""

from app.database import SessionLocal
from app import crud, schemas
from datetime import date, timedelta
import random

def add_sample_employees():
    db = SessionLocal()
    
    sample_employees = [
        {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "+1234567890",
            "department": "Engineering",
            "position": "Senior Software Engineer",
            "salary": 95000.00,
            "hire_date": date(2022, 1, 15),
            "address": "123 Main St, New York, NY 10001",
            "is_active": True
        },
        {
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@example.com",
            "phone": "+1234567891",
            "department": "Marketing",
            "position": "Marketing Manager",
            "salary": 85000.00,
            "hire_date": date(2021, 6, 20),
            "address": "456 Oak Ave, Los Angeles, CA 90001",
            "is_active": True
        },
        {
            "first_name": "Bob",
            "last_name": "Johnson",
            "email": "bob.johnson@example.com",
            "phone": "+1234567892",
            "department": "Engineering",
            "position": "DevOps Engineer",
            "salary": 88000.00,
            "hire_date": date(2022, 3, 10),
            "address": "789 Pine Rd, Chicago, IL 60601",
            "is_active": True
        },
        {
            "first_name": "Alice",
            "last_name": "Williams",
            "email": "alice.williams@example.com",
            "phone": "+1234567893",
            "department": "Human Resources",
            "position": "HR Specialist",
            "salary": 65000.00,
            "hire_date": date(2023, 1, 5),
            "address": "321 Elm St, Houston, TX 77001",
            "is_active": True
        },
        {
            "first_name": "Charlie",
            "last_name": "Brown",
            "email": "charlie.brown@example.com",
            "phone": "+1234567894",
            "department": "Sales",
            "position": "Sales Representative",
            "salary": 70000.00,
            "hire_date": date(2022, 9, 15),
            "address": "654 Maple Dr, Phoenix, AZ 85001",
            "is_active": False
        }
    ]
    
    added_count = 0
    for emp_data in sample_employees:
        # Check if employee already exists
        existing = crud.get_employee_by_email(db, emp_data["email"])
        if not existing:
            employee = schemas.EmployeeCreate(**emp_data)
            crud.create_employee(db, employee)
            added_count += 1
            print(f"✅ Added: {emp_data['first_name']} {emp_data['last_name']}")
        else:
            print(f"⚠️ Skipped (already exists): {emp_data['first_name']} {emp_data['last_name']}")
    
    db.close()
    print(f"\n📊 Added {added_count} new employees to database")

if __name__ == "__main__":
    print("Adding sample employee data...")
    add_sample_employees()
    print("Done!")