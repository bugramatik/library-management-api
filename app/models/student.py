from pydantic import BaseModel

# Model used when creating a new student
class StudentCreate(BaseModel):
    name: str
    department: str

# Model used when retrieving or updating a student
class Student(StudentCreate):
    id: int

    class Config:
        orm_mode = True
