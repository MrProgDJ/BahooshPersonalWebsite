#!/bin/bash
set -e
echo "Running migrations..."
python manage.py migrate --noinput
echo "Collecting static files..."
python manage.py collectstatic --noinput 2>&1 || true
echo "Creating admin user..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@bahoosh.com', 'admin123')
    print('Admin user created successfully!')
else:
    print('Admin user already exists.')
"
echo "Starting gunicorn..."
exec gunicorn config.wsgi --bind 0.0.0.0:$PORT
