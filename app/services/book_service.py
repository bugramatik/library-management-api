from sqlalchemy.orm import Session
from ..database.models import Book as BookModel


def get_all_books(db: Session) -> object:
    return db.query(BookModel).all()


def get_book_by_id(db: Session, book_id: int) -> object:
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if book is None:
        raise ValueError("Book not found!")
    return book


def create_book(db: Session, book: dict):
    book = BookModel(**book.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def update_book(db: Session, book_id: int, book):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    db.delete(db_book)
    db.commit()
    return db_book
