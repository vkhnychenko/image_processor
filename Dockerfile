FROM python:3.8-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py migrate