# Dev Dockerfile
FROM python:latest

MAINTAINER ['Abhijit Maity', 'abhijit.maity2010@gmail.com']

# Force stdin, stdout and stderr - buffer
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
VOLUME ["/code"]
ADD . /code/
RUN pip install -r requirements.txt
EXPOSE 8080