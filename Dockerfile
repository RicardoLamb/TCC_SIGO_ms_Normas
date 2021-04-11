FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv && pipenv install --system

COPY . /app/