
# Makefile
install:
	poetry install

PORT ?= 8000
run:
	poetry run python manage.py migrate
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi

dev:
	poetry run python manage.py migrate
	poetry run python manage.py runserver
translate:
	 poetry run django-admin makemessages -l ru
build_translate:
	poetry run django-admin compilemessages