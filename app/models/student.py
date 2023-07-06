from pydantic import BaseModel


class Student(BaseModel):
    id: int
    name: str
    department: str

    class Config:
        orm_mode = True
