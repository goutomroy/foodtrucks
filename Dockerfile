FROM python:3.11-alpine

RUN mkdir /app

WORKDIR /app

RUN apk add --no-cache gcc musl-dev python3-dev
RUN apk add --no-cache gdal-bin libgdal-dev python3-gdal
RUN apk add --no-cache python3-gdal
RUN apk add --no-cache binutils libproj-dev
RUN pip install -U pip setuptools wheel ruamel.yaml.clib

COPY requirements requirements

RUN pip install -r requirements/development.txt

COPY . .

LABEL maintainer="Goutom Roy" version="1.0.0"
