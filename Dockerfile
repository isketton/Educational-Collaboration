FROM python:3.12-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc 
RUN mkdir /code
WORKDIR /code
COPY requirements.txt .
COPY .env .
RUN pip install -r requirements.txt
COPY . .