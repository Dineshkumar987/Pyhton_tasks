# ============================================================
# 🔐 FastAPI STUDENT MANAGEMENT + JWT Authentication
#                    (Array Version)
# ============================================================
 
# ============================================================
# 🚀 WHAT WE ARE BUILDING
# ============================================================
 
'''
This project includes:
 
✅ FastAPI
✅ JWT Authentication
✅ CRUD Operations
✅ Temporary Storage using Python List
✅ Protected Student APIs using Token
 
No Database used here.
Student data will be stored temporarily in array/list.
'''
 
 
# ============================================================
# 🚀 INSTALL REQUIRED PACKAGES
# ============================================================
 
'''
pip install fastapi uvicorn python-jose
'''
 
 
# ============================================================
# 📦 IMPORTS
# ============================================================
 
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from typing import List
 
 
# ============================================================
# 🚀 CREATE FASTAPI APP
# ============================================================
 
app = FastAPI()
 
 
# ============================================================
# 🔐 JWT CONFIGURATION
# ============================================================
 
'''
SECRET_KEY
-----------
 
Used to sign the token.
 
Think:
 
JWT Token = Locked Box
SECRET_KEY = Key to lock/unlock
 
If secret key changes:
Old tokens become invalid.
'''
 
SECRET_KEY = "mysecretkey"
 
 
# ------------------------------------------------------------
 
'''
ALGORITHM
-----------
 
Algorithm used to create JWT token.
 
HS256 = Common JWT algorithm
'''
 
ALGORITHM = "HS256"
 
 
# ------------------------------------------------------------
 
'''
TOKEN EXPIRY TIME
-----------------
 
Token will expire after 5 minutes.
'''
 
ACCESS_TOKEN_EXPIRE = timedelta(minutes=5)
 
 
# ============================================================
# 🧾 PYDANTIC MODELS
# ============================================================
 
'''
Student Model
-------------
 
Used for:
 
- Request validation
- Student data structure
- Automatic API documentation
'''
 
 
class Student(BaseModel):
 
    name: str
    age: int
    course: str
    marks: int
 
 
# ------------------------------------------------------------
 
'''
Login Model
-----------
 
Used for username and password.
'''
 
 
class Login(BaseModel):
 
    username: str
    password: str
 
 
# ============================================================
# 🗃️ TEMPORARY STUDENT DATABASE
# ============================================================
 
'''
Temporary array/list storage.
 
⚠️ Data will be lost when server restarts.
'''
 
students: List[dict] = []
 
 
# ============================================================
# 🔐 CREATE JWT TOKEN
# ============================================================
 
def create_access_token(data: dict):
 
    '''
    Steps:
 
    1. Copy incoming data
    2. Create expiry time
    3. Add expiry time
    4. Encode JWT token
    5. Return token
    '''
 
    # Copy data
 
    to_encode = data.copy()
 
 
    # Create expiry time
 
    expire = datetime.now(timezone.utc) + ACCESS_TOKEN_EXPIRE
 
 
    # Add expiry into payload
 
    to_encode.update({
        "exp": expire
    })
 
 
    # Generate JWT token
 
    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
 
 
    return encoded_jwt
 
 
# ============================================================
# 🔐 TOKEN VALIDATION
# ============================================================
 
'''
OAuth2PasswordBearer
--------------------
 
Automatically:
 
- Reads Authorization header
- Extracts Bearer token
 
Example:
 
Authorization: Bearer eyJhbGc...
'''
 
 
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)
 
 
# ------------------------------------------------------------
 
def verify_token(
    token: str = Depends(oauth2_scheme)
):
 
    '''
    This function validates token.
 
    Steps:
 
    1. Read token
    2. Decode token
    3. Verify secret key
    4. Verify expiry time
    5. Extract username
    '''
 
    try:
 
        # Decode JWT token
 
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
 
 
        # Extract username
 
        username = payload.get("sub")
 
 
        # Check username exists
 
        if username is None:
 
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
 
 
        return username
 
 
    except JWTError:
 
        '''
        Happens when:
 
        - Token expired
        - Wrong secret key
        - Invalid token
        '''
 
        raise HTTPException(
            status_code=401,
            detail="Token expired or invalid"
        )
 
 
# ============================================================
# 🏠 HOME API
# ============================================================
 
@app.get("/")
def home():
 
    return {
        "message": "Student Management System + JWT + Array 🚀"
    }
 
 
# ============================================================
# 🔐 LOGIN API
# ============================================================
 
@app.post("/login")
def login(user: Login):
 
    '''
    Dummy Login
 
    Username = admin
    Password = admin123
    '''
 
 
    if (
        user.username != "admin"
        or
        user.password != "admin123"
    ):
 
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
 
 
    '''
    Create JWT token.
 
    "sub" = subject/user
    '''
 
    access_token = create_access_token(
        data={
            "sub": user.username
        }
    )
 
 
    return {
 
        "access_token": access_token,
 
        "token_type": "bearer",
 
        "expires_in": "5 minutes"
    }
 
 
# ============================================================
# ➕ CREATE STUDENT
# ============================================================
 
@app.post("/students")
def add_student(
 
    student: Student,
 
    user: str = Depends(verify_token)
 
):
 
    '''
    Depends(verify_token)
 
    Means:
 
    Before API executes:
        verify_token() runs
 
    If token is invalid:
        API stops immediately
 
    If token is valid:
        Student will be added
    '''
 
 
    # Generate Student ID
 
    new_id = len(students) + 1
 
 
    # Create new student
 
    new_student = {
 
        "id": new_id,
 
        "name": student.name,
 
        "age": student.age,
 
        "course": student.course,
 
        "marks": student.marks
    }
 
 
    # Add student to list
 
    students.append(new_student)
 
 
    return {
 
        "message": "Student added successfully",
 
        "data": new_student
    }
 
 
# ============================================================
# 📋 READ ALL STUDENTS
# ============================================================
 
@app.get("/students")
def get_all_students(
 
    user: str = Depends(verify_token)
 
):
 
    '''
    Flow:
 
    1. Read Authorization Header
    2. Extract Bearer Token
    3. verify_token() runs
    4. jwt.decode() validates:
        - Secret key
        - Expiry
        - Algorithm
    5. If valid:
        Continue API
    6. If expired:
        Return 401 Error
    '''
 
 
    return {
 
        "count": len(students),
 
        "data": students
    }
 
 
# ============================================================
# 🔍 READ SINGLE STUDENT
# ============================================================
 
@app.get("/students/{student_id}")
def get_student(
 
    student_id: int,
 
    user: str = Depends(verify_token)
 
):
 
    '''
    Find student using ID.
    '''
 
 
    for student in students:
 
        if student["id"] == student_id:
 
            return student
 
 
    raise HTTPException(
 
        status_code=404,
 
        detail="Student not found"
    )
 
 
# ============================================================
# ✏️ UPDATE STUDENT
# ============================================================
 
@app.put("/students/{student_id}")
def update_student(
 
    student_id: int,
 
    updated_student: Student,
 
    user: str = Depends(verify_token)
 
):
 
    '''
    Update existing student.
    '''
 
 
    for index, student in enumerate(students):
 
        if student["id"] == student_id:
 
 
            # Keep original ID
 
            students[index] = {
 
                "id": student_id,
 
                "name": updated_student.name,
 
                "age": updated_student.age,
 
                "course": updated_student.course,
 
                "marks": updated_student.marks
            }
 
 
            return {
 
                "message": "Student updated successfully",
 
                "data": students[index]
            }
 
 
    raise HTTPException(
 
        status_code=404,
 
        detail="Student not found"
    )
 
 
# ============================================================
# 🗑️ DELETE STUDENT
# ============================================================
 
@app.delete("/students/{student_id}")
def delete_student(
 
    student_id: int,
 
    user: str = Depends(verify_token)
 
):
 
    '''
    Delete student using ID.
    '''
 
 
    for index, student in enumerate(students):
 
        if student["id"] == student_id:
 
 
            deleted = students.pop(index)
 
 
            return {
 
                "message": "Student deleted successfully",
 
                "data": deleted
            }
 
 
    raise HTTPException(
 
        status_code=404,
 
        detail="Student not found"
    )
 
 
# ============================================================
# 🔥 FINAL JWT FLOW
# ============================================================
 
'''
LOGIN FLOW
----------
 
Client Login
    ↓
POST /login
    ↓
Username + Password
    ↓
Generate JWT Token
    ↓
Return Token to Client
 
 
API ACCESS FLOW
---------------
 
Client Calls Student API
    ↓
Send Token in Header
 
Authorization:
Bearer eyJhbGc...
 
    ↓
verify_token() runs
    ↓
jwt.decode() validates:
 
    ✅ Secret Key
    ✅ Expiry Time
    ✅ Algorithm
 
    ↓
 
If Valid:
    Continue Student API
 
If Expired:
    Return 401 Error
'''
 
 
# ============================================================
# 🌐 RUN SERVER
# ============================================================
 
'''
uvicorn Student_Token:app --reload
'''
 
 
# ============================================================
# 🌐 SWAGGER DOCS
# ============================================================
 
'''
http://127.0.0.1:8000/docs
'''