FROM python:3.11-slim AS BASE

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /sneakers_api

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
