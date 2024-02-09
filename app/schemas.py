from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class CourseBase(BaseModel):
    name: str
    city: str
    state: str
    par: int

class CourseCreate(BaseModel):
    name: str
    city: str
    state: str
    par: int

class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True

class ScoreBase(BaseModel):
    round_id: int
    hole_number: int
    score: int

class ScoreCreate(ScoreBase):
    pass

class ScoreRoundCreate(BaseModel):
    scores: List[ScoreBase]

class Score(ScoreBase):
    id: int

    class Config:
        orm_mode = True

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
