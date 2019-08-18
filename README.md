# Metrolyrics Scraper

Example project using Scrapy to extract lyrics of top artists from metrolyrics.com and store them into a PostGres database.

### Components:
- Scrapy project template for structuring code (i.e. via ``scrapy startproject``)
- **items.py** for creating custom scraped items.
- **pipelines.py** for creating a custom pipeline for sending scraped items into local PostGres database.
- SQLAlchemy object-relational-mapper (ORM) for creating the connection to PostGres and inserting data without directly writing SQL queries.
- **model.py** file (*new addition*) to setup up Model-View-Controller (MVC) architecture for SQL Alchemy ORM.

### How to run:
- start at the root directory of the repository (i.e. where the *scrapy.cfg* file is located)
- make sure you have a local Postgres server running! (e.g. localhost, port 5432).
- in Postgres, have a database already created, called **metrolyrics**. (e.g. ``creatdb metrolyrics``)
- make sure you have sqlalchemy installed (e.g. ``pip install sqlalchemy``)
- run ``scrapy crawl lyrics``


## Still to-do:
- add middleware to use proxy IPs / different user agents.
