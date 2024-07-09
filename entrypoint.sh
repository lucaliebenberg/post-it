#!/bin/sh

python manage.py makemigrations postms accounts authors jobposts
python manage.py migrate
python manage.py collectstatic

gunicorn postms.wsgi:application --bind 0.0.0.0:8000
