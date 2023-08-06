# Build image as
# docker build --tag python-sphinx .

FROM python:3.7-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN /usr/local/bin/python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apk update 
RUN apk add --no-cache make