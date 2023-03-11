from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "yo what is going on"}