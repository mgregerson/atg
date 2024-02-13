from pydantic import BaseModel
from datetime import date
from typing import List
from .scoreSchemas import Score

class RoundBase(BaseModel):
    user_id: int
    course_id: int
    date: date

class RoundCreate(RoundBase):
    pass

class Round(RoundBase):
    id: int

    scores: List[Score] = []

    class Config:
        orm_mode = True