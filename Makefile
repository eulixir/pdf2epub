.PHONY: run

run:
	PYTHONPATH=. uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

format:
	black app
	black tests

lint:
	ruff check app
	ruff check tests