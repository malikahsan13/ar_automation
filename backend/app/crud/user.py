from app.models.user import User
from app.core.security import hash_password, verify_password
from sqlalchemy.orm import Session

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, email: str, password: str):
    db_user = User(email = email, hashed_password=hash_password(password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user