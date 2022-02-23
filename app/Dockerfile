FROM python:3.9.10

ARG DJANGO_ENV

ADD hive_sbi_webapp          /app/hive_sbi_webapp
ADD requirements             /app/requirements
ADD requirements.txt         /app/requirements.txt
ADD boot_scripts             /app/boot_scripts
ADD manage.py                /app/manage.py

WORKDIR /app/

RUN apt-get update
RUN pip install --upgrade pip; \
	pip install -r requirements/$DJANGO_ENV.txt

RUN adduser --disabled-password --gecos '' app

ENV HOME /home/app
ENV DJANGO_SETTINGS_MODULE hive_sbi_webapp.settings.$DJANGO_ENV
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV DJANGO_ENV $DJANGO_ENV

CMD sh /app/boot_scripts/$DJANGO_ENV.sh