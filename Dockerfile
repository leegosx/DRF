FROM python:3.11.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip \
  && pip install poetry

WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /app/

COPY .env /app/
RUN while read line; do export "$line"; done < /app/.env

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
