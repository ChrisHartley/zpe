ZPEIT - Zoning, Permits, Enforcement Information Tool


Tools to scrape Accella, save the resulting cases in a django app,
send emails notifying users of cases within their defined areas of interest

Docker
- Django app
  - sqlite3 as db
- Gunicorn
- nginix
- Selenium Firefox
  - scraper


Pre-defined areas of interest
- Zipcodes
- Townships
- Defined neighborhoods


# Dev

## Run Django Server

1. `docker compose --profile production up --build`
