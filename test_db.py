from sqlalchemy import text
from app.database import engine, SessionLocal

def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("✅ Database connection successful!")
            
            # Get MySQL version
            result = conn.execute(text("SELECT VERSION()"))
            version = result.fetchone()[0]
            print(f"📦 MySQL Version: {version}")
            
            return True
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

def test_create_table():
    from app.database import Base
    from app import models
    
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created/verified")

def list_tables():
    with SessionLocal() as db:
        result = db.execute(text("SHOW TABLES"))
        tables = [row[0] for row in result]
        print(f"📋 Tables in database: {tables}")

if __name__ == "__main__":
    print("Testing MySQL Connection\n" + "="*50)
    
    if test_connection():
        test_create_table()
        list_tables()
        print("\n✨ Database is ready for use!")
    else:
        print("\n⚠️ Please check:")
        print("1. XAMPP MySQL is running")
        print("2. Database 'employee_management' exists")
        print("3. Credentials are correct")