from app.database import engine, Base
from app import models
import pymysql

def init_database():
    """Initialize database tables"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")

def check_connection():
    """Test database connection"""
    try:
        from sqlalchemy import text
        with engine.connect() as conn:
            result = conn.execute(text("SELECT VERSION()"))
            version = result.fetchone()[0]
            print(f"Connected to MySQL version: {version}")
            return True
    except Exception as e:
        print(f"Connection failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing MySQL connection...")
    if check_connection():
        init_database()
        print("Database setup complete!")
    else:
        print("Please make sure XAMPP MySQL is running on port 3306")