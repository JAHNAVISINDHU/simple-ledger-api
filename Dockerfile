FROM python:3.11-slim

WORKDIR /code

# system deps for psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY ./alembic.ini ./
COPY ./migrations ./migrations
COPY .env.example .env

ENV PYTHONUNBUFFERED=1
ENV PATH=/root/.local/bin:$PATH

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
