# simple-ledger-api

Advanced Simple Ledger API (FastAPI + PostgreSQL + Docker + Alembic)

## What is included
- FastAPI backend with endpoints for accounts & transactions
- Running balance & formatted ledger response
- Alembic migrations (migrations/versions/0001_initial.py)
- Docker + docker-compose to run DB + API
- Swagger UI: `/docs`

## Quick start (Docker)
1. Build & start:
```bash
docker-compose build --no-cache
docker-compose up
