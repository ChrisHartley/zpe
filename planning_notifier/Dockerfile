# syntax=docker/dockerfile:1
FROM python:3.12
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#COPY ../Pipfile /code
WORKDIR /code
RUN pip install pipenv
COPY ./Pipfile ./Pipfile.lock /code/
COPY . /code/
RUN pipenv install --system --deploy && apt-get update && apt-get upgrade -y && apt-get install -y binutils libproj-dev gdal-bin libsqlite3-mod-spatialite
RUN chmod a+x /code/planning_notifier/start-local.sh
