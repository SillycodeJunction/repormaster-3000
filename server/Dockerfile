FROM mysql:latest

MAINTAINER me

ENV MYSQL_DATABASE=reportmaster \
    MYSQL_ROOT_PASSWORD=password

ADD schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306