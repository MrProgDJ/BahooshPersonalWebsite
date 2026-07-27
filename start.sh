#!/bin/bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput
exec gunicorn config.wsgi --bind 0.0.0.0:$PORT
