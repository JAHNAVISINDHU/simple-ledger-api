from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app import schemas, crud, services

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post("/", response_model=schemas.AccountResponse)
def create_account(account: schemas.AccountCreate, db: Session = Depends(get_db)):
    return crud.create_account(db, account)


@router.get("/", response_model=list[schemas.AccountResponse])
def list_accounts(db: Session = Depends(get_db)):
    return crud.get_accounts(db)


@router.get("/{account_id}/ledger")
def get_account_ledger(account_id: int, db: Session = Depends(get_db)):
    account = crud.get_account(db, account_id)
    if not account:
        raise HTTPException(404, "Account not found")
    return services.format_ledger(db, account_id)
