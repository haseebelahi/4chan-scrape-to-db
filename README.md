# 4chan-scrape-to-db
Scrapes a specific board on 4chan and dumps the board threads and comments on threads into a PostgreSQL DB for further processing

# Setup Instructions

- Python 3.7 needed
- PostgreSQL 10.6
- Create a new PostgreSQL database
- Run the database creation script (db_creation.sql)
- Update the db connection settings in db_helper.py
- Update board name in scrape.py
- Run `python scrape.py`
