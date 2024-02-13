from sqlalchemy.orm import Session
from app import models
from app.schemas import courseSchemas

def get_course_by_name(db: Session, name: str):
    return db.query(models.Course).filter(models.Course.name == name).first()

def create_course(db: Session, course: courseSchemas.CourseCreate):
    db_course = models.Course(name=course.name, city=course.city, state=course.state, par=course.par, zip_code=course.zip_code)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()