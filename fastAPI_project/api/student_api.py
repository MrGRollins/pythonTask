from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from fastAPI_project.db.models.base_model import StudentModel, GroupModel
from fastAPI_project.dependencies.persistence import group_persistence_dependency

app = FastAPI()

# Создать студента
@app.post("/students")
def create_student(student: StudentModel, session: Session = Depends(group_persistence_dependency)):
    db_student = StudentModel(
        first_name=student.first_name,
        last_name=student.last_name,
        age=student.age
    )
    session.add(db_student)
    session.commit()
    session.refresh(db_student)
    return db_student

# Получить информацию о студенте по его id
@app.get("/students/{student_id}")
def get_student(student_id: int, session: Session = Depends(group_persistence_dependency)):
    student = session.query(StudentModel).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Удалить студента
@app.delete("/students/{student_id}")
def delete_student(student_id: int, session: Session = Depends(group_persistence_dependency)):
    student = session.query(StudentModel).get(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    session.delete(student)
    session.commit()
    return {"message": "Student deleted"}

# Получить список студентов
@app.get("/students", response_model=List[StudentModel])
def get_students(session: Session = Depends(group_persistence_dependency)):
    students = session.query(StudentModel).all()
    return students

# Добавить студента в группу
@app.post("/groups/{group_id}/add_student/{student_id}")
def add_student_to_group(group_id: int, student_id: int, session: Session = Depends(group_persistence_dependency)):
    group = session.query(GroupModel).get(group_id)
    student = session.query(StudentModel).get(student_id)

    if group is None:
        return {"error": "Group not found"}

    if student is None:
        return {"error": "Student not found"}

    group.students.append(student)
    session.commit()

    return {"message": "Student added to group successfully"}
