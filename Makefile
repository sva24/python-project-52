
# Makefile
install:
	poetry install

PORT ?= 8000
run:
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi

dev:
	poetry run python manage.py runserver