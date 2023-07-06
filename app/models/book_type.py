from pydantic import BaseModel


class BookType(BaseModel):
    id: int
    subject_name: str

    class Config:
        orm_mode = True
