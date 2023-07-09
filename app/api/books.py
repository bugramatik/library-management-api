from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.book import Book
from ..services.book_service import get_all_books, get_book_by_id, create_book, update_book, delete_book

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}}, )


@router.get("/", response_model=List[Book])
def get_books(db: Session = Depends(get_db)):
    return get_all_books(db)


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    try:
        return get_book_by_id(db, book_id)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create", response_model=Book)
def create_new_book(book: Book, db: Session = Depends(get_db)):
    try:
        return create_book(db, book)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update/{book_id}", response_model=Book)
def update_existing_book(book_id: int, book: Book, db: Session = Depends(get_db)):
    try:
        return update_book(db, book_id, book)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/remove/{book_id}", response_model=Book)
def delete_existing_book(book_id: int, db: Session = Depends(get_db)):
    try:
        return delete_book(db, book_id)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))