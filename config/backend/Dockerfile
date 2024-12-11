# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
#COPY requirements.txt /code/
#RUN pip install -r requirements.txt
RUN pip install pipenv
COPY ./Pipfile ./Pipfile.lock /code/
RUN pipenv install --system --deploy && apt-get update && apt-get upgrade -y && apt-get install -y binutils libproj-dev gdal-bin libsqlite3-mod-spatialite
COPY ./backend .
COPY ./config/backend/start.sh .
RUN chmod +x /code/start.sh
