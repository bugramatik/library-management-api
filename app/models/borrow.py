from pydantic import BaseModel


class Borrow(BaseModel):
    student_id: int
    book_id: int

    class Config:
        orm_mode = True
