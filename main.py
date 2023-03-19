from fastapi import FastAPI
from resources.routes import api_router


app = FastAPI()
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "yo what is going on"}