#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python /code/planning_notifier/manage.py migrate
cd /code/planning_notifier
gunicorn --bind=0.0.0.0 backend.wsgi
