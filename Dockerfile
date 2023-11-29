FROM python:3.11

RUN mkdir /app

WORKDIR /app

RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin libpq-dev &&\
    apt-get clean

COPY requirements requirements

RUN pip install -r requirements/development.txt

COPY . .

LABEL maintainer="Goutom Roy" version="1.0.0"
