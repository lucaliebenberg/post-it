#!/bin/sh

set -e

echo "Waiting for database..."

while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done

echo "Database started"

python manage.py migrate
python manage.py collectstatic --no-input

exec gunicorn postms.wsgi:application --bind 0.0.0.0:8000
