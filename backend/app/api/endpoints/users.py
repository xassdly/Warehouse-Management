from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models import user as models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users")
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.post("/users")
def create_user(username: str, password: str, role: str, db: Session = Depends(get_db)):
    db_user = models.User(username=username, password=password, role=role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user