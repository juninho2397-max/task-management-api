# Task Management API

A clean REST API built with FastAPI, SQLAlchemy and SQLite. The project demonstrates typed schemas, persistence, CRUD operations, dependency injection and automated testing.

## Endpoints
- `GET /health`
- `POST /tasks`
- `GET /tasks`
- `PATCH /tasks/{id}`
- `DELETE /tasks/{id}`

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Interactive API documentation is available at `/docs`.

## Tests
```bash
pytest -q
```
