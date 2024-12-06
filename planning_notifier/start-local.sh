#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python /code/manage.py migrate
python /code/manage.py runserver 0.0.0.0:8000
#cd /code/backend
#gunicorn --bind=0.0.0.0 backend.wsgi