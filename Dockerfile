FROM python:3.7-alpine
MAINTAINER Deep Ease Alex

ENV PYTHONUNBUFFERED 1

COPY ./req.txt /req.txt
RUN pip3 install -r /req.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
