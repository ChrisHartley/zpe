#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python /code/planning_notifier/manage.py makemigrations
python /code/planning_notifier/manage.py migrate
python /code/planning_notifier/manage.py runserver 0.0.0.0:8000
