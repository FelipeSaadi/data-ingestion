.PHONY: up install test run

up:
	docker-compose up

install:
	poetry install

test:
	poetry run pytest tests/

run:
	poetry run python app.py

all: install test run