from fastapi import FastAPI
from .routers import accounts, transactions

app = FastAPI(title="Simple Ledger API")

app.include_router(accounts.router)
app.include_router(transactions.router)


@app.get("/")
def root():
    return {"message": "Simple Ledger API is running!"}
