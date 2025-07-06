from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"))