from fastapi import FastAPI
from app.routes import auth
from app.database import engine
from app import models
from app.models.user import Base


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "歡迎來到天氣預報"}


