FROM python:3.10

WORKDIR /app

ENV PYTHONUNBUFFERED 1

RUN pip install gunicorn

COPY . /app

COPY ./requirements.txt /app/requirements.txt


RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app


