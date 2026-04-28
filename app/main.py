from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import employees

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Management System",
    description="REST API for managing employees",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employees.router, prefix="/api/v1", tags=["employees"])

@app.get("/")
def root():
    return {
        "message": "Welcome to Employee Management System API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "database": "MySQL"}