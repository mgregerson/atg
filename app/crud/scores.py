from sqlalchemy.orm import Session
from app import models
from app.schemas import scoreSchemas
from typing import List

def create_score(db: Session, score: scoreSchemas.ScoreCreate):
    db_score = models.Score(round_id=score.round_id, hole_number=score.hole_number, score=score.score)
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

def create_scores_for_full_round(db: Session, round_id: int, scores: List[scoreSchemas.ScoreBase]):
    db_scores = []
    for score_data in scores:
        db_score = models.Score(round_id=round_id, hole_number=score_data.hole_number, score=score_data.score)
        db.add(db_score)
        db_scores.append(db_score)
    db.commit()
    return db_scores