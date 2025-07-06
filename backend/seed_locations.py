from app.core.database import SessionLocal
from app.models import location as models

def seed_locations():
    db = SessionLocal()
    locations = [
        models.Location(name=f"{row}-{str(shelf).zfill(2)}-{str(bin).zfill(2)}")
        for row in range(10,41)
        for shelf in range(1,41)
        for bin in range(1,5)
    ]


    db.add_all(locations)
    db.commit()
    db.close()
    print("Seeded locations")

if __name__ == "__main__":
    seed_locations()