from fastapi import FastAPI , Path, BackgroundTasks, HTTPException
from typing import Optional
from pydantic import BaseModel
import os
app = FastAPI()

students = {
    1:{
        "name":"john",
        "age":17,
        "year":"year 12"
    },
    2:{
        "name":"ibo",
        "age":17,
        "year":"year 12"
    }
}

class Student(BaseModel):
    name : str
    age : int
    year : str

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/get-student/{student_id}")
def get_students(student_id : int = Path(description="The ID of student you want to view",gt=0,lt=54)):
    return students[student_id]

@app.get("/get-by-name")
def get_student(students_id:Optional[int]= None , name : Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    # if students[students_id] == students[students_id]:
    #     return students[students_id]
    return {"Data": "Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"error":"Student exists"}

    students[student_id] = student
    return students[student_id]

@app.put("/update-Student/{student_id}")
def update_student(student_id : int, student:StudentUpdate):
    if student_id not in students:
        return {"Error":"Student does not exists"}
    if student.name != None:
        students[student_id].name= student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error":"Does not exists"}

    del students[student_id]
    return {"messager":"deleted"}

