from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from ..database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)