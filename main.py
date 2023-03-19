from fastapi import FastAPI
import uvicorn
from resources.routes import api_router
from db import database

app = FastAPI()
app.include_router(api_router)

@app.on_event("startup")
async def startup():
    await database.connect()
    
@app.on_event("shutdown")
async def start():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)