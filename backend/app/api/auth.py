from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.crud.user import get_user_by_email, create_user
from app.core.security import verify_password, create_access_token
from app.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
        

@router.post("/register", response_model=UserOut)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user.email, user.password)

@router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}