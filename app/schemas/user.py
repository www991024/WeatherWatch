from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    line_user_id: str = None

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str = None

class PasswordReset(BaseModel):
    email: EmailStr
    new_password: str

class ResetPasswordRequest(BaseModel):
    email:EmailStr
    

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    line_user_id: str = None

    class Config:
         from_attributes = True