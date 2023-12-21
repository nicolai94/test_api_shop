#!/bin/sh
APP_PORT=${PORT:-8000}
python manage.py collectstatic --noinput --clear &
python manage.py makemigrations --noinput &
python manage.py migrate --noinput &
python manage.py runserver "0.0.0.0:${APP_PORT}"