#!/bin/bash

rm db.sqlite3
rm -rf ./runnerapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations runnerapi
python3 manage.py migrate runnerapi
python3 manage.py loaddata user
python3 manage.py loaddata runner
python3 manage.py loaddata park
python3 manage.py loaddata event