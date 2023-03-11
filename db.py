import dataclasses
import sqlalchemy
from decouple import config

DATABASE_URL = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@localhost:5432"
database = dataclasses.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()