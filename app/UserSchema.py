from pydantic import BaseModel
from datetime import date
from typing import List, Optional
from .schemas import Round

class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    rounds: List[Round] = []

    class Config:
        orm_mode = True