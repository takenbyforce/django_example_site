#!/bin/bash

PROCESS_TYPE=$1

if [ "$PROCESS_TYPE" = "server" ]; then
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic --noinput
    if [ "$DJANGO_SUPERUSER_USERNAME" ]
    then
        python manage.py createsuperuser \
            --noinput \
            --username "$DJANGO_SUPERUSER_USERNAME" \
            --email "$DJANGO_SUPERUSER_EMAIL"
    fi
    python manage.py runserver 0.0.0.0:8080
elif [ "$PROCESS_TYPE" = "flower" ]; then
    celery \
        -A django_example_site \
        flower \
        -l INFO \
        --broker="${CELERY_BROKER}"
elif [ "$PROCESS_TYPE" = "worker" ]; then
    celery \
        -A django_example_site \
        worker \
        -l INFO
fi