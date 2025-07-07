from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models import location as models
from app.models import item as item_models
from app.core.security import verify_user # test

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/protected") # test
def get_protected(user: str = Depends(verify_user)):
    return {"message": f"Hello {user}, role: {user["role"]}"}

@router.get("/locations")
def read_locations(db: Session = Depends(get_db)):
    return db.query(models.Location).all()

@router.get("/locations/{location_id}")
def read_location(location_id: int, db: Session = Depends(get_db)):
    return db.query(models.Location).filter(models.Location.id == location_id).first()

@router.get("/locations/{location_id}/items")
def read_location_items(location_id: int, db: Session = Depends(get_db)):
    return db.query(item_models.Item).filter(item_models.Item.location_id == location_id).all()

