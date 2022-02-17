# hive_sbi_webapp

Basic docs


Create virtualenv

~~~
python3 -m venv env
~~~


python manage.py runserver localhost:8010



Docker compose deployment
=========================


### Network

Create a network with the `bridge` driver:

~~~
$ docker network create --driver bridge sbi-bridge
~~~

### Set environment variables

Generate a new `.env` file from the provided template:

~~~
$ cp env.template .env
~~~

Example of `.env` file:

~~~
LANG=C.UTF-8
LC_ALL=C.UTF-8

~~~


# DEVELOPMENT ENVIRONMENT

### Build image

~~~
$ PORT_NGINX=5000 PORT_DEBUG=8000 IMAGE_SERVICE=$(basename $PWD) docker-compose --project-directory=$(pwd) -f compose/docker-compose.base.yml -f compose/docker-compose.dev.yml build
~~~

### run service

~~~
$ PORT_NGINX=5000 PORT_DEBUG=8000 IMAGE_SERVICE=$(basename $PWD) docker-compose --project-directory=$(pwd) -f compose/docker-compose.base.yml -f compose/docker-compose.dev.yml up
~~~


