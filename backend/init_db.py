from app.core.database import Base, engine
from app.models import item

print("Creating tables in the database...")

Base.metadata.create_all(bind=engine)

print("Done!")