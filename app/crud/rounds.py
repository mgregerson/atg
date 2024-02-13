from sqlalchemy.orm import Session
from app import models
from app.schemas import roundSchemas

def get_round_by_id(db: Session, round_id: int):
    return db.query(models.Round).filter(models.Round.id == round_id).first()

def create_round(db: Session, round: roundSchemas.RoundCreate):
    db_round = models.Round(user_id=round.user_id, course_id=round.course_id, date=round.date)
    db.add(db_round)
    db.commit()
    db.refresh(db_round)
    return db_round
