#!/bin/bash
echo "Check if the database exists and create it if it doesn't"
python manage.py check_database

echo "Applying database migrations..."
python manage.py makemigrations 
python manage.py migrate

echo "Applying admin user..."
python manage.py init_data

exec "$@"