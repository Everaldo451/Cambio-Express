#!/bin/sh
poetry run python src/manage.py migrate
poetry run python src/manage.py collectstatic
poetry run python src/manage.py runserver $HOST:$PORT
#poetry run gunicorn src.backend.wsgi:application