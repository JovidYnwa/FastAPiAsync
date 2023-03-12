import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from decouple import config

DATABASE_URL = f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}@localhost:5432"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

Base = declarative_base()
