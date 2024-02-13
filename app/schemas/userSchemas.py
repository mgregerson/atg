from pydantic import BaseModel
from typing import List
from .roundSchemas import Round


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