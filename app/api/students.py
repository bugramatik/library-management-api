from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.student import Student, StudentCreate
from ..models.book import Book
from ..services import student_service

router = APIRouter(
    prefix="/students",
    tags=["students"],
    responses={404: {"description": "Not found"}}, )


@router.get("/", response_model=list[Student])
def get_students(db: Session = Depends(get_db)):
    return student_service.get_students(db)


@router.post("/", response_model=Student)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return student_service.create_student(db, student)


@router.get("/{student_id}", response_model=Student)
def get_student(student_id: int, db: Session = Depends(get_db)):
    try:
        return student_service.get_student_by_id(db, student_id)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    try:
        return student_service.update_student(db, student_id, student)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{student_id}", response_model=Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    try:
        return student_service.delete_student(db, student_id)
    except ValueError as e:
        return HTTPException(status_code=500, detail=str(e))


@router.get("/{student_id}/borrowed_books", response_model=list[Book])
def get_borrowed_books(student_id: int, db: Session = Depends(get_db)):
    try:
        return student_service.get_borrowed_books(db, student_id)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
