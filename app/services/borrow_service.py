from sqlalchemy.orm import Session
from ..database.models import Book as BookModel, Borrow as BorrowModel, Student as StudentModel


def borrow_book(db: Session, student_id: int, book_id: int):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()

    if db_book is None:
        raise ValueError("Book not found!")
    elif db_student is None:
        raise ValueError("Student not found!")
    elif db_book.copy_number < 1:
        raise ValueError("No available copies of the book!")
    elif db.query(BorrowModel).filter(BorrowModel.book_id == book_id, BorrowModel.student_id == student_id).first() is not None:
        raise ValueError("Student already borrowed this book!")
    elif len(db_student.borrowed_books) >= 3:
        raise ValueError("Student already borrowed 3 books!")
    borrow = BorrowModel(student_id=student_id, book_id=book_id)
    db.add(borrow)
    db_book.copy_number -= 1  # decrease the number of copies
    db.commit()
    db.refresh(borrow)

    return borrow


def return_book(db: Session, borrow_id: int):
    db_borrow = db.query(BorrowModel).filter(BorrowModel.id == borrow_id).first()
    if db_borrow is None:
        raise ValueError("Borrow not found!")

    db_book = db.query(BookModel).filter(BookModel.id == db_borrow.book_id).first()
    db.delete(db_borrow)
    db_book.copy_number += 1  # increase the number of copies
    db.commit()

    return {"message": "Book returned successfully"}
