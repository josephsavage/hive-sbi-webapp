#!/bin/sh

mkdir /home/app/logs

touch /home/app/logs/gunicorn-access.log
touch /home/app/logs/gunicorn.log
tail -n 0 -f /home/app/logs/*.log &

chown -R app:app /app
chown -R app:app /home/app

python manage.py migrate
python manage.py collectstatic --noinput

exec su -m app -c 'gunicorn hive_sbi_webapp.wsgi -b :8000 \
    --access-logfile /home/app/logs/gunicorn-access.log \
    --error-logfile /home/app/logs/gunicorn.log'
