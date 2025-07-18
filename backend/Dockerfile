FROM python:3.12.10-slim

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false
RUN poetry install --without dev test --no-root

ENV ENV=production
ENV HOST=0.0.0.0
ENV PORT=8000

EXPOSE 8000

COPY . .
CMD [ "sh", "run.sh" ]