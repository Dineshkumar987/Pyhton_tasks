# ============================================================
# 🎓 FastAPI Student Management CRUD - MySQL
#
# Install:
# python -m pip install fastapi uvicorn sqlalchemy pymysql
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session


# ------------------------------------------------------------
# 🚀 FastAPI App
# ------------------------------------------------------------

app = FastAPI()


# ------------------------------------------------------------
# 🗄️ MySQL Configuration
# ------------------------------------------------------------

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/student_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


# ------------------------------------------------------------
# 🧱 Database Table Model
# ------------------------------------------------------------

class StudentDB(Base):
    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    name = Column(String(100))
    age = Column(Integer)
    course = Column(String(100))
    marks = Column(Integer)


# ------------------------------------------------------------
# Create Table Automatically
# ------------------------------------------------------------

Base.metadata.create_all(bind=engine)


# ------------------------------------------------------------
# 🧾 Pydantic Student Model
# ------------------------------------------------------------

class Student(BaseModel):
    name: str
    age: int
    course: str
    marks: int


# ------------------------------------------------------------
# 🔌 Database Dependency
# ------------------------------------------------------------

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# ------------------------------------------------------------
# 🏠 Q1. Create FastAPI Application
# ------------------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Student Management System is started"
    }


# ------------------------------------------------------------
# ➕ Q2. Add Student
# ------------------------------------------------------------

@app.post("/students")
def add_student(
    student: Student,
    db: Session = Depends(get_db)
):

    new_student = StudentDB(
        name=student.name,
        age=student.age,
        course=student.course,
        marks=student.marks
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Student added successfully"
    }


# ------------------------------------------------------------
# 📋 Q3. Get All Students
# ------------------------------------------------------------

@app.get("/students")
def get_all_students(
    db: Session = Depends(get_db)
):

    students = db.query(StudentDB).all()

    return students


# ------------------------------------------------------------
# 🔍 Q4. Get Student by ID
# ------------------------------------------------------------

@app.get("/students/{id}")
def get_student_by_id(
    id: int,
    db: Session = Depends(get_db)
):

    student = db.query(StudentDB).filter(
        StudentDB.id == id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# ------------------------------------------------------------
# ✏️ Q5. Update Student
# ------------------------------------------------------------

@app.put("/students/{id}")
def update_student(
    id: int,
    updated_student: Student,
    db: Session = Depends(get_db)
):

    student = db.query(StudentDB).filter(
        StudentDB.id == id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = updated_student.name
    student.age = updated_student.age
    student.course = updated_student.course
    student.marks = updated_student.marks

    db.commit()
    db.refresh(student)

    return {
        "message": "Student updated successfully"
    }


# ------------------------------------------------------------
# 🗑️ Q6. Delete Student
# ------------------------------------------------------------

@app.delete("/students/{id}")
def delete_student(
    id: int,
    db: Session = Depends(get_db)
):

    student = db.query(StudentDB).filter(
        StudentDB.id == id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }


# ------------------------------------------------------------
# ▶️ Run Server
# ------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "MYSQL_main:app",
        reload=True
    )