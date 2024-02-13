from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app import models
from app.schemas import courseSchemas, roundSchemas, scoreSchemas, userSchemas
from app.crud import courses, rounds, users, scores
from app.database.db import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=userSchemas.User)
def create_user(user: userSchemas.UserCreate, db: Session = Depends(get_db)):
    db_user = users.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return users.create_user(db=db, user=user)

@app.get("/users/", response_model=List[userSchemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users_data = users.get_users(db, skip=skip, limit=limit)
    return users_data

@app.get("/users/{user_id}", response_model=userSchemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = users.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get('/courses', response_model=List[courseSchemas.Course])
def get_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_courses = courses.get_courses(db, skip=skip, limit=limit)
    return db_courses

@app.post("/courses", response_model=courseSchemas.Course)
def create_course(course: courseSchemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = courses.get_course_by_name(db, name=course.name)
    if db_course:
        raise HTTPException(status_code=400, detail="Course already exists")
    return courses.create_course(db=db, course=course)

@app.post("/rounds", response_model=roundSchemas.Round)
def create_round(round: roundSchemas.RoundCreate, db: Session = Depends(get_db)):
    return rounds.create_round(db=db, round=round)

@app.get("/rounds/{round_id}", response_model=roundSchemas.Round)
def read_round(round_id: int, db: Session = Depends(get_db)):
    db_round = rounds.get_round_by_id(db, round_id=round_id)
    if db_round is None:
        raise HTTPException(status_code=404, detail="Round not found")
    return db_round

@app.post("/scores", response_model=scoreSchemas.Score)
def create_score(score: scoreSchemas.ScoreCreate, db: Session = Depends(get_db)):
    # TODO: Check that the user hasn't created a score for this hole already
    return scores.create_score(db=db, score=score)

@app.post("/scores/{round_id}", response_model=List[scoreSchemas.Score])
def create_score_for_round(round_id: int, score: scoreSchemas.ScoreRoundCreate, db: Session = Depends(get_db)):
    return scores.create_scores_for_full_round(db=db, round_id=round_id, scores=score.scores)

# supabase = create_supabase_client()

# app.get("/")(lambda: {"Hello": "World"})

# @app.get("/users/")
# def get_all_users(db: Session = Depends(get_db)):
#     return db.query(User).all()

# @app.get("/users/{username}")
# def get_user_by_email(username: str, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.username == username).first()
#     if user:
#         return user
#     raise HTTPException(status_code=404, detail="User not found")

# @app.post("/users/")
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = User(username=user.username, email=user.email, password=user.password, first_name=user.first_name, last_name=user.last_name, is_admin=user.is_admin)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# @app.put("/users/{username}")
# def update_user_by_email(username: str, user: UserUpdate, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.username == username).first()
#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")
#     db_user.first_name = user.first_name
#     db_user.last_name = user.last_name
#     db_user.email = user.email
#     db.commit()
#     return {"message": "User updated successfully"}


# @app.delete("/users/{user_id}")
# def delete_user_by_email(user_id: int, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.id == user_id).first()
#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")
#     db.delete(db_user)
#     db.commit()
#     return {"message": "User deleted successfully"}
