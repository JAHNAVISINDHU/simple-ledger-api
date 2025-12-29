from sqlalchemy.orm import Session
from .crud import get_transactions_by_account


def format_ledger(db: Session, account_id: int):
    txs = get_transactions_by_account(db, account_id)

    balance = 0
    ledger = []

    for t in txs:
        if t.type.lower() == "credit":
            balance += t.amount
        else:
            balance -= t.amount

        ledger.append({
            "id": t.id,
            "amount": t.amount,
            "type": t.type,
            "description": t.description,
            "timestamp": t.timestamp,
            "running_balance": balance
        })

    return {"account_id": account_id, "balance": balance, "ledger": ledger}
