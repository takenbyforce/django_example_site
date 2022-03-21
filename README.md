# django_example_site

## Setting up

### Install Docker and docker-compose
See installation
instructions at [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

 ## Starting up
Start the container by executing:
```bash
$ docker-compose up
```

## Available pages
Admin: http://localhost:8000/admin/

API: http://localhost:8000/api/

Flower: http://localhost:5557/

## Default admin user
Default credentials are: `admin:TemporaryPwd2022`

This superuser created in `docker-entrypoint.sh`. Credentials can be changed in `.env` file 

## Running tests
To run test inside docker container
```bash
docker exec -it django_example_site_web_1 bash
./manage.py test -v2
```
