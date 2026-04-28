from sqlalchemy.orm import Session
from typing import Optional, List
from app import models, schemas

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def get_employee_by_email(db: Session, email: str):
    return db.query(models.Employee).filter(models.Employee.email == email).first()

def get_employees(db: Session, skip: int = 0, limit: int = 100, department: Optional[str] = None, is_active: Optional[bool] = None):
    query = db.query(models.Employee)
    
    if department:
        query = query.filter(models.Employee.department == department)
    if is_active is not None:
        query = query.filter(models.Employee.is_active == is_active)
    
    total = query.count()
    employees = query.offset(skip).limit(limit).all()
    
    return total, employees

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee(db: Session, employee_id: int, employee_update: schemas.EmployeeUpdate):
    db_employee = get_employee(db, employee_id)
    if not db_employee:
        return None
    
    update_data = employee_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_employee, field, value)
    
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = get_employee(db, employee_id)
    if not db_employee:
        return False
    
    db.delete(db_employee)
    db.commit()
    return True