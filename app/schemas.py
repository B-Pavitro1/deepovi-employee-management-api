from pydantic import BaseModel, EmailStr, Field, validator
from datetime import date
from typing import Optional

class EmployeeBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=20)
    department: str = Field(..., min_length=1, max_length=50)
    position: str = Field(..., min_length=1, max_length=50)
    salary: float = Field(..., gt=0)
    hire_date: date
    address: Optional[str] = None
    is_active: bool = True
    
    @validator('hire_date')
    def validate_hire_date(cls, v):
        if v > date.today():
            raise ValueError('Hire date cannot be in the future')
        return v

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = Field(None, min_length=1, max_length=50)
    last_name: Optional[str] = Field(None, min_length=1, max_length=50)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=20)
    department: Optional[str] = Field(None, min_length=1, max_length=50)
    position: Optional[str] = Field(None, min_length=1, max_length=50)
    salary: Optional[float] = Field(None, gt=0)
    hire_date: Optional[date] = None
    address: Optional[str] = None
    is_active: Optional[bool] = None

class EmployeeResponse(EmployeeBase):
    id: int
    
    class Config:
        from_attributes = True