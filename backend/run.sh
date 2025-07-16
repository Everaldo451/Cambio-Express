poetry run python src/manage.py makemigrations 
poetry run python src/manage.py migrate 
poetry run gunicorn src.backend.wsgi:application