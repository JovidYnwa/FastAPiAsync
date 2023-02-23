import databases
from fastapi import FastAPI, Request
import sqlalchemy 
import os, sys
from decouple import config

DATABASE_URL=f"postgresql+psycopg2://{config('DB_USER')}:{config('DB_PASSWORD')}@localhost:5432"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

books = sqlalchemy.Table(
    "books",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("author", sqlalchemy.String),
)

reades = sqlalchemy.Table(
    "readers",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
)

readers_books = sqlalchemy.Table(
    "readers_books",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("book_id", sqlalchemy.ForeignKey("books.id"), nullable=False),
    sqlalchemy.Column("reader_id", sqlalchemy.ForeignKey("readers.id"), nullable=False),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/books")
async def get_all_books():
    query = books.select()
    return await database.fetch_all(query)

@app.post("/books")
async def create_books(requst: Request):
    data = await requst.json()
    query = books.insert().values(**data)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}

@app.post("/readers")
async def create_books(requst: Request):
    data = await requst.json()
    query = reades.insert().values(**data)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}

@app.post("/read")
async def create_books(requst: Request):
    data = await requst.json()
    query = readers_books.insert().values(**data)
    last_record_id = await database.execute(query)
    return {"id": last_record_id}