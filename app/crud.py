from sqlalchemy.orm import Session
from . import models, schemas, UserSchema
from typing import List

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserSchema.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, password=fake_hashed_password, first_name=user.first_name, last_name=user.last_name, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_course_by_name(db: Session, name: str):
    return db.query(models.Course).filter(models.Course.name == name).first()

def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(name=course.name, city=course.city, state=course.state, par=course.par)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()

def get_round_by_id(db: Session, round_id: int):
    return db.query(models.Round).filter(models.Round.id == round_id).first()

def create_round(db: Session, round: schemas.RoundCreate):
    db_round = models.Round(user_id=round.user_id, course_id=round.course_id, date=round.date)
    db.add(db_round)
    db.commit()
    db.refresh(db_round)
    return db_round

def create_score(db: Session, score: schemas.ScoreCreate):
    db_score = models.Score(round_id=score.round_id, hole_number=score.hole_number, score=score.score)
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

def create_scores_for_full_round(db: Session, round_id: int, scores: List[schemas.ScoreBase]):
    db_scores = []
    for score_data in scores:
        db_score = models.Score(round_id=round_id, hole_number=score_data.hole_number, score=score_data.score)
        db.add(db_score)
        db_scores.append(db_score)
    db.commit()
    return db_scores