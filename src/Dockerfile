FROM python:3.10.2

WORKDIR /app

COPY ./requiremets.txt /app

RUN pip install -m requiremets.txt --no-cache-dir

COPY . /app

