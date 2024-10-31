from sqlalchemy import create_engine
from app.database import DATABASE_URL, metadata

def create_tables():
    engine = create_engine(DATABASE_URL)
    metadata.create_all(engine)
    print("Tables 新增成功.")

if __name__ == "__main__":
    create_tables()