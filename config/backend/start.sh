#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python /code/backend/manage.py migrate
cd /code/backend
gunicorn --bind=0.0.0.0 backend.wsgi
