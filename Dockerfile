FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app

ENTRYPOINT ["./docker-entrypoint.sh"]

