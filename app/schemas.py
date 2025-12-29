from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AccountCreate(BaseModel):
    name: str
    type: str


class AccountResponse(BaseModel):
    id: int
    name: str
    type: str

    class Config:
        orm_mode = True


class TransactionCreate(BaseModel):
    account_id: int
    amount: float
    type: str
    description: Optional[str] = None


class TransactionResponse(BaseModel):
    id: int
    account_id: int
    amount: float
    type: str
    description: Optional[str]
    timestamp: datetime

    class Config:
        orm_mode = True
