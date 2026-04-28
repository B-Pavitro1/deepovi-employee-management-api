from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

pymysql.install_as_MySQLdb()

# MySQL Database Configuration
# Update password if you set one in XAMPP
MYSQL_USER = "root"
MYSQL_PASSWORD = ""  # Leave empty if no password
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DATABASE = "employee_management"

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"charset": "utf8mb4"},
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False  # Set to True to see SQL queries
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()