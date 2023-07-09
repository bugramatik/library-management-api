from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..database.models import Borrow as BorrowModel
from ..services import borrow_service
from ..models.borrow import Borrow as BorrowSchema

router = APIRouter(
    prefix="/cashier",
    tags=["cashier"],
    responses={404: {"description": "Not found"}}, )


@router.post("/borrow", response_model=BorrowSchema)
def lend_book(borrow: BorrowSchema, db: Session = Depends(get_db)):
    try:
        return borrow_service.borrow_book(db, **borrow.dict())
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/return/{borrow_id}")
def return_book(borrow_id: int, db: Session = Depends(get_db)):
    try:
        return borrow_service.return_book(db, borrow_id)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))

