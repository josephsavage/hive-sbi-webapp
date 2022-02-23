# hive_sbi_webapp

Docker compose  V3.7 deployment
===============================


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

SECRET_KEY=XXXSecretXKEY
SBI_API_URL= https://api.steembasicincome.com
~~~

**Change SECRET_KEY for a long and secure string.**

# DEVELOPMENT ENVIRONMENT

### Build app image

~~~
$ PORT_NGINX=5008 PORT_DEBUG=8008 IMAGE_SERVICE=$(basename $PWD) docker-compose --project-directory=$(pwd) -f compose/docker-compose.base.yml -f compose/docker-compose.dev.yml build
~~~

### run service

~~~
$ PORT_NGINX=5008 PORT_DEBUG=8008 IMAGE_SERVICE=$(basename $PWD) docker-compose --project-directory=$(pwd) -f compose/docker-compose.base.yml -f compose/docker-compose.dev.yml up
~~~

Application will be exposed on port http://localhost:8008 and through NGINX on port http://localhost:5008.


# PRODUCTION ENVIRONMENT

### Build app image

~~~
$ docker build app -t hive_sbi_webapp:0.1.0 --build-arg DJANGO_ENV=prod
~~~

### run service

~~~
$ PORT_NGINX=5008 PORT_DEBUG=8008 IMAGE_SERVICE=$(basename $PWD) docker-compose --project-directory=$(pwd) -f compose/docker-compose.base.yml -f compose/docker-compose.prod.yml up -d
~~~

Application will be exposed through NGINX on port http://localhost:5008.


Docker compose V2 deployment
============================


For Docker versions 18.xx or lower it could be necessary to deploy with compose V2 files.


### run service

~~~
$ docker-compose -f prod.yml up -d
~~~
