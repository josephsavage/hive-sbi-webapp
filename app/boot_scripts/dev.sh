#!/bin/sh

# evita error de permisos
chown -R app:app /app
chown -R app:app /home/app

python manage.py migrate
python manage.py collectstatic --noinput

exec su -m app -c 'python manage.py runserver_plus 0.0.0.0:8008'