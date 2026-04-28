from sqlalchemy import Column, Integer, String, Float, Date, Boolean, Text, DECIMAL
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    phone = Column(String(20), nullable=True)
    department = Column(String(50), nullable=False)
    position = Column(String(50), nullable=False)
    salary = Column(DECIMAL(10, 2), nullable=False)
    hire_date = Column(Date, nullable=False)
    address = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"<Employee {self.first_name} {self.last_name}>"