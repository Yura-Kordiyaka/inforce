#!/bin/bash

set -e

# Очікування доступності PostgreSQL бази даних
/app/wait-for-it.sh pgdb:5432 -- python /app/inforce/manage.py migrate

# Запуск сервера Django
python /app/inforce/manage.py runserver 0.0.0.0:8000