#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations --empty users
python manage.py makemigrations users
python manage.py makemigrations --empty ecommerce
python manage.py makemigrations ecommerce
python manage.py migrate
