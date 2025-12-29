from sqlalchemy.orm import Session
from . import models, schemas


# Accounts
def create_account(db: Session, account: schemas.AccountCreate):
    db_account = models.Account(name=account.name, type=account.type)
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account


def get_accounts(db: Session):
    return db.query(models.Account).all()


def get_account(db: Session, account_id: int):
    return db.query(models.Account).filter(models.Account.id == account_id).first()


# Transactions
def create_transaction(db: Session, tx: schemas.TransactionCreate):
    db_tx = models.Transaction(
        account_id=tx.account_id,
        amount=tx.amount,
        type=tx.type,
        description=tx.description
    )
    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)
    return db_tx


def get_transactions(db: Session):
    return db.query(models.Transaction).all()


def get_transactions_by_account(db: Session, account_id: int):
    return db.query(models.Transaction).filter(
        models.Transaction.account_id == account_id
    ).all()
