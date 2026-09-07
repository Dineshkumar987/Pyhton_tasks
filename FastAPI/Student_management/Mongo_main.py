# ============================================================
# 🎓 FastAPI Student Management CRUD - MongoDB Atlas + MongoEngine
# pip install fastapi uvicorn mongoengine pymongo certifi
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import connect, Document, IntField, StringField
import certifi

# ------------------------------------------------------------
# 🚀 FastAPI App
# ------------------------------------------------------------

app = FastAPI()

# ------------------------------------------------------------
# 🌐 MongoDB Atlas Connection
# ------------------------------------------------------------

MONGO_URL = "mongodb+srv://vangaridinesh60_db_user:Dinesh60@cluster0.hbzq9vk.mongodb.net/student_db?retryWrites=true&w=majority"

connect(
    host=MONGO_URL,
    tlsCAFile=certifi.where()
)

# ------------------------------------------------------------
# 🧱 MongoDB Model
# ------------------------------------------------------------

class StudentDB(Document):

    id = IntField(primary_key=True)
    name = StringField(required=True)
    age = IntField(required=True)
    course = StringField(required=True)
    marks = IntField(required=True)

    meta = {
        "collection": "students"
    }

# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------

class Student(BaseModel):

    name: str
    age: int
    course: str
    marks: int

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------

@app.get("/")
def home():

    return {
        "message": "Student Management System is started"
    }

# ------------------------------------------------------------
# ✅ 1. CREATE STUDENT
# ------------------------------------------------------------

@app.post("/students")
def add_student(student: Student):

    # Find the last student ID
    last_student = StudentDB.objects.order_by("-id").first()

    if last_student:
        new_id = last_student.id + 1
    else:
        new_id = 1

    new_student = StudentDB(
        id=new_id,
        name=student.name,
        age=student.age,
        course=student.course,
        marks=student.marks
    )

    new_student.save()

    return {
        "message": "Student added successfully"
    }

# ------------------------------------------------------------
# ✅ 2. READ ALL STUDENTS
# ------------------------------------------------------------

@app.get("/students")
def get_all_students():

    students = StudentDB.objects()

    data = []

    for student in students:

        data.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "course": student.course,
            "marks": student.marks
        })

    return data

# ------------------------------------------------------------
# ✅ 3. READ SINGLE STUDENT
# ------------------------------------------------------------

@app.get("/students/{id}")
def get_student_by_id(id: int):

    student = StudentDB.objects(id=id).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "course": student.course,
        "marks": student.marks
    }

# ------------------------------------------------------------
# ✅ 4. UPDATE STUDENT
# ------------------------------------------------------------

@app.put("/students/{id}")
def update_student(
    id: int,
    updated_student: Student
):

    student = StudentDB.objects(id=id).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = updated_student.name
    student.age = updated_student.age
    student.course = updated_student.course
    student.marks = updated_student.marks

    student.save()

    return {
        "message": "Student updated successfully"
    }

# ------------------------------------------------------------
# ✅ 5. DELETE STUDENT
# ------------------------------------------------------------

@app.delete("/students/{id}")
def delete_student(id: int):

    student = StudentDB.objects(id=id).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.delete()

    return {
        "message": "Student deleted successfully"
    }

# ------------------------------------------------------------
# ▶️ Run Server
# ------------------------------------------------------------

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "Mongo_main:app",
        reload=True
    )