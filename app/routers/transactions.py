from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app import schemas, crud

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/", response_model=schemas.TransactionResponse)
def create_transaction(tx: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, tx)


@router.get("/", response_model=list[schemas.TransactionResponse])
def list_transactions(db: Session = Depends(get_db)):
    return crud.get_transactions(db)
