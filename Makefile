
# Makefile
install:
	poetry install

run:
	poetry run gunicorn task_manager.wsgi

dev:
	poetry run python manage.py runserver