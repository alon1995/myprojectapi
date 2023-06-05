FROM python:3.10-slim

WORKDIR /project1

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install Django psycopg2-binary djangorestframework django-cors-headers

COPY . .

CMD python manage.py runserver 0.0.0.0:8000