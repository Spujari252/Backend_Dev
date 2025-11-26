from typing import Union
from random import randint

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class StudentCreate(BaseModel):
    first_name: str
    last_name: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/status")
def get_status():
    return {"message": "ok"}


@app.post("/students/")
def create_student(student: StudentCreate):
    # Minimal in-memory creation for tests: validate payload and return a generated id.
    student_id = randint(1, 10_000_000)
    return {"id": student_id}
