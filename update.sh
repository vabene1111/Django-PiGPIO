#!/usr/bin/env bash
docker-compose run web_pigpio python3 manage.py migrate
docker-compose run web_pigpio python3 manage.py collectstatic --noinput
