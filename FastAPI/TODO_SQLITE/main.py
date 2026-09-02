# ============================================================
# 📝 FastAPI TODO App (CRUD) - SQLite Database Version
# ============================================================

from typing import Optional
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# ------------------------------------------------------------
# 🚀 Create FastAPI App
# ------------------------------------------------------------
app = FastAPI(title="FastAPI TODO SQLite")

# ------------------------------------------------------------
# 🗄️ Database Configuration
# ------------------------------------------------------------
DATABASE_URL = "sqlite:///./todos.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ------------------------------------------------------------
# 🧱 Database Model (Table)
# ------------------------------------------------------------
class TodoDB(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)

# Create table schema in database
Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------
# 🧾 Pydantic Schemas
# ------------------------------------------------------------
class TodoCreate(BaseModel):
    title: str
    completed: bool = False

class TodoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    completed: bool

# ------------------------------------------------------------
# 🔌 Dependency (DB Session)
# ------------------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.get("/")
def home():
    return {"message": "FastAPI TODO with SQLite DB 🚀"}

# ------------------------------------------------------------
# ✅ 1. CREATE TODO
# ------------------------------------------------------------
@app.post("/todos")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = TodoDB(
        title=todo.title,
        completed=todo.completed
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return {"message": "Todo created successfully", "data": new_todo}

# ------------------------------------------------------------
# ✅ 2. READ ALL TODOS
# ------------------------------------------------------------
@app.get("/todos")
def get_all_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoDB).all()
    return {"count": len(todos), "data": todos}

# ------------------------------------------------------------
# ✅ 3. READ SINGLE TODO
# ------------------------------------------------------------
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo

# ------------------------------------------------------------
# ✅ 4. UPDATE TODO
# ------------------------------------------------------------
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated: TodoCreate, db: Session = Depends(get_db)):
    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo.title = updated.title
    todo.completed = updated.completed

    db.commit()
    db.refresh(todo)

    return {"message": "Updated successfully", "data": todo}

# ------------------------------------------------------------
# ✅ 5. DELETE TODO
# ------------------------------------------------------------
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoDB).filter(TodoDB.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(todo)
    db.commit()

    return {"message": "Deleted successfully"}

# ------------------------------------------------------------
# ▶️ Run Server
# ------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)