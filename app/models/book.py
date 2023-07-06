from pydantic import BaseModel


class Book(BaseModel):
    id: int
    name: str
    author: str
    copy_number: int
    book_type_id: int

    class Config:
        orm_mode = True
