from fastapi import FastAPI
from db_connect import get_connection
app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}


