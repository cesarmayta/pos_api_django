#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
#python manage.py createsuperuser --no-input --username
#python manage.py createsuperuser2 --username admin --password Tecsup2022
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'cmayta@tecsup.edu.pe', 'Tecsup2022')" | python manage.py shell