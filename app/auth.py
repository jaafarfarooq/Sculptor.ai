# app/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from app.models.user import User
from .utils import hash_password, verify_password, create_access_token

router = APIRouter(tags=["auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(username: str, password: str, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(400, "Username already registered")
    user = User(username=username, hashed_password=hash_password(password))
    db.add(user)
    db.commit()
    return {"msg": "User created"}

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(400, "Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
