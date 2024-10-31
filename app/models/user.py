from sqlalchemy import Column, Integer, String
from app.database import Base
from pydantic import BaseModel, EmailStr

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    line_user_id = Column(String, unique=True, index=True, nullable=True)



class ResetPasswordRequest(BaseModel):
    email: EmailStr
