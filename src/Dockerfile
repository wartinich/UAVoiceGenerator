FROM python:3.10.2

WORKDIR /app

COPY ./req.txt /app

RUN pip install --upgrade pip
RUN pip install -r req.txt --no-cache-dir

COPY . /app

