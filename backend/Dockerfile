FROM python:3.12.10-slim

RUN apt-get update -y
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential pkg-config

RUN pip install poetry

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME=/etc/poetry

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN poetry install --without dev --without test --no-root

ENV ENV=production
ENV HOST=0.0.0.0
ENV PORT=8000

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=backend.settings
ENV PYTHONPATH=/app/src:/app

COPY . .

RUN chmod +x run.sh
CMD ["./run.sh" ]