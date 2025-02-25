from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from datetime import datetime
from ..database.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text)
    image_url = Column(String(255))
    category = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
