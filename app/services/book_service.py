from sqlalchemy.orm import Session
from ..database.models import Book as BookModel, BookType as BookTypeModel


def get_all_books(db: Session) -> object:
    return db.query(BookModel).all()


def get_book_by_id(db: Session, book_id: int) -> object:
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if book is None:
        raise ValueError("Book not found!")
    return book


def create_book(db: Session, book: dict):
    # Check if the book type exists
    db_book_type = db.query(BookTypeModel).filter(BookTypeModel.id == book.book_type_id).first()
    if db_book_type is None:
        raise ValueError("Book type not found!")

    # Check if the optional id field is exists
    if book.id is not None:
        # Check if a book with the same id already exists
        db_book_id = db.query(BookModel).filter(BookModel.id == book.id).first()
        if db_book_id is not None:
            raise ValueError("Appointed id already exists!")

    # Check if a book with the same name and author already exists
    db_book = db.query(BookModel).filter(BookModel.name == book.name, BookModel.author == book.author).first()

    # If a book with the same name and author exists, raise an error
    if db_book is not None:
        raise ValueError("Book already exists!")

    db_book = BookModel(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


def update_book(db: Session, book_id: int, book):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if db_book is None:
        raise ValueError("Book not found!")
    db_book_type = db.query(BookTypeModel).filter(BookTypeModel.id == book.book_type_id).first()

    if db_book_type is None:
        raise ValueError("Book type not found!")

    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if db_book is None:
        raise ValueError("Book not found!")

    db.delete(db_book)
    db.commit()
    return db_book
