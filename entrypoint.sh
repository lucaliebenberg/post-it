#!/bin/sh

# python manage.py makemigrations postms accounts authors jobposts
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn postms.wsgi:application --bind 0.0.0.0:8000
