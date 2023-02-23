# FastApi Async

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/JovidYnwa/FastAPiAsync
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Docker-compose on server:

```sh
docker-compose build
docker-compose up
```


Making Migrations alimbic:

```sh
alembic init migrations
docker-compose run app alembic revision --autogenerate -m "name_of_migration" 
docker-compose run app alembic upgrade head
```

Populating DB with data:

```sh
docker-compose run app python populate.py
```