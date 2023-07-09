from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..database.models import Student as StudentModel
from ..models.student import StudentCreate


def get_students(db: Session):
    return db.query(StudentModel).all()


def get_student_by_id(db: Session, student_id: int):
    db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


def create_student(db: Session, student: StudentCreate):
    db_student = StudentModel(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student(db: Session, student_id: int, student_update: StudentCreate):
    db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()

    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in student_update.dict().items():
        setattr(db_student, key, value)
    db.commit()
    db.refresh(db_student)
    return db_student


def delete_student(db: Session, student_id: int):
    db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()

    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(db_student)
    db.commit()
    return db_student


def get_borrowed_books(db: Session, student_id: int):
    db_student = db.query(StudentModel).filter(StudentModel.id == student_id).first()

    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Add book details from borrow table
    borrowed_books_list = []
    for borrow in db_student.borrowed_books:
        borrowed_books_list.append(borrow.book)
    return borrowed_books_list
