from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.future import select
from app import models, schemas
from app.database import get_db
from app.utils.auth import verify_password, get_password_hash, create_access_token, get_current_user
from app.schemas.user import PasswordReset,ResetPasswordRequest,UserLogin
from app.models.user import User
from app.config import settings
from passlib.hash import bcrypt
from app.core.security import verify_password
import jwt
import os


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/login")
async def login(credentials: UserLogin, db: AsyncSession = Depends(get_db)):
    result =  db.execute(select(User).where(User.username==credentials.username))
    user = result.scalar_one_or_none()

    if user and bcrypt.verify(credentials.password, user.hashed_password):
        token_data = {"sub": credentials.username}
        token = jwt.encode(token_data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}
    
    raise HTTPException(status_code=401, detail="用戶名或密碼錯誤")


@router.post("/register", response_model=schemas.user.Token)
def register(user: schemas.user.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == User.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="使用者已存在")
    
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password, line_user_id=user.line_user_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/token", response_model=schemas.user.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="帳號或密碼錯誤",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/reset-password-request")
def reset_password_request(request: ResetPasswordRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="找不到使用者")

    return {"message": "密碼重置連結傳送到你的Email"}

@router.post("/reset-password")
def reset_password(reset_data: PasswordReset, db: Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.email == reset_data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.hashed_password = get_password_hash(reset_data.new_password)
    db.commit()
    return {"message": "密碼重置成功"}

@router.get("/me", response_model=schemas.user.User)
def read_users_me(current_user: models.user.User = Depends(get_current_user)):
    return current_user

