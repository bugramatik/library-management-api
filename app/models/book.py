from typing import Optional

from pydantic import BaseModel, NonNegativeInt


class Book(BaseModel):
    id: Optional[int]
    name: str
    author: str
    copy_number: NonNegativeInt
    book_type_id: Optional[int] = None

    class Config:
        orm_mode = True
