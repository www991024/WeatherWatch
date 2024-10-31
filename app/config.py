import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    WEATHERREPORT_ACCESS_TOKEN = os.getenv("WEATHERREPORT_ACCESS_TOKEN")
    WEATHERREPORT_SECRET = os.getenv("WEATHERREPORT_SECRET")
settings = Settings()