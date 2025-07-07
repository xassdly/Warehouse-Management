#!/usr/bin/env python3
"""
Setup script for the Warehouse Management API
This script initializes the database and seeds it with initial data.
"""

import os
import sys

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.core.database import Base, engine
from app.models import user, item, location, order
from app.core.database import SessionLocal
from app.models import location as location_models

def init_database():
    """Initialize the database with all tables"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

def seed_locations():
    """Seed the database with location data"""
    print("Seeding locations...")
    db = SessionLocal()
    
    # Check if locations already exist
    existing_locations = db.query(location_models.Location).count()
    if existing_locations > 0:
        print(f"Locations already exist ({existing_locations} found). Skipping seeding.")
        db.close()
        return
    
    locations = [
        location_models.Location(name=f"{row}-{str(shelf).zfill(2)}-{str(bin).zfill(2)}")
        for row in range(10, 41)
        for shelf in range(1, 41)
        for bin in range(1, 5)
    ]
    
    db.add_all(locations)
    db.commit()
    db.close()
    print(f"Seeded {len(locations)} locations successfully!")

def main():
    """Main setup function"""
    print("Setting up Warehouse Management API...")
    
    # Initialize database
    init_database()
    
    # Seed locations
    seed_locations()
    
    print("Setup completed successfully!")
    print("\nTo run the API server, use:")
    print("cd backend")
    print("uvicorn app.main:app --reload")

if __name__ == "__main__":
    main() 