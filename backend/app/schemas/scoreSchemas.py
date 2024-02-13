from pydantic import BaseModel
from typing import List

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