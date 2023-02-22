import databases
from fastapi import FastAPI, Request
import sqlalchemy 

import os, sys

DATABASE_URL="postgresql+psycopg2://postgres:password@localhost:5432"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

books = sqlalchemy.Table(
    "books",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("author", sqlalchemy.String),
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