#!/bin/sh
poetry run python src/manage.py migrate
poetry run python src/manage.py collectstatic
poetry run gunicorn -c gunicorn.conf.py src.backend.wsgi:application --bind $HOST:$PORT