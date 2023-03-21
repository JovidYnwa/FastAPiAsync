from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from resources.routes import api_router
from db import database

origins = [
    "http://localhost",
    "http://localhost:4200"
]


app = FastAPI()
app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_orogins=origins,
    allow_methods=["*"],
    allow_headers=["*"],    
)


@app.on_event("startup")
async def startup():
    await database.connect()
    
@app.on_event("shutdown")
async def start():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)