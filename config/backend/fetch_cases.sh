#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset
python /code/planning_notifier/manage.py fetch_cases
