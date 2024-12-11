#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python /code/backend/manage.py migrate
python /code/backend/manage.py runserver 0.0.0.0:8000
