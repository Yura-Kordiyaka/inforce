FROM python:3.10

WORKDIR /app

ENV PYTHONUNBUFFERED 1

RUN pip install gunicorn

COPY . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

COPY ./wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

ENTRYPOINT ["/app/inforce/docker/python/entrypoint.sh"]
