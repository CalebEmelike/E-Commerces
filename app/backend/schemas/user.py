from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    first_name: str
    last_name: str
    password: str

class UserLogin(UserBase):
    password: str

class User(UserBase):
    id: int
    first_name: str
    last_name: str
    created_at: datetime

    class Config:
        from_attributes = True