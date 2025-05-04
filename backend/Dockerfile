FROM python:3.12.10-slim

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false
RUN poetry install --without dev test --no-root

COPY . .
CMD ["sh","-c","python src/manage.py makemigrations && python src/manage.py migrate && python run.py"]