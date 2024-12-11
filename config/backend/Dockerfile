# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
RUN pip install pipenv
COPY ./Pipfile ./Pipfile.lock /code/
RUN pipenv install --system --deploy && apt-get update && apt-get upgrade -y && apt-get install -y binutils libproj-dev gdal-bin libsqlite3-mod-spatialite
COPY ./planning_notifier .
COPY ./config/backend/start.sh .
RUN chmod +x /code/start.sh
#RUN chmod +x ./config/backend/start.sh
CMD ["/code/start.sh"]
