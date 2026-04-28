from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import Optional
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/employees", response_model=schemas.EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    existing_employee = crud.get_employee_by_email(db, employee.email)
    if existing_employee:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Employee with this email already exists"
        )
    return crud.create_employee(db=db, employee=employee)

@router.get("/employees", response_model=dict)
def list_employees(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    department: Optional[str] = None,
    is_active: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    total, employees = crud.get_employees(db=db, skip=skip, limit=limit, department=department, is_active=is_active)
    return {"total": total, "employees": employees}

@router.get("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return employee

@router.put("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def update_employee(employee_id: int, employee_update: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    if employee_update.email:
        existing_employee = crud.get_employee_by_email(db, employee_update.email)
        if existing_employee and existing_employee.id != employee_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    employee = crud.update_employee(db, employee_id, employee_update)
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return employee

@router.delete("/employees/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    success = crud.delete_employee(db, employee_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return None