from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), index=True)
    first_name = Column(String(50), index=True)
    last_name = Column(String(50), index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String(50))
    rounds = relationship("Round", back_populates="user")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    city = Column(String(50), index=True)
    state = Column(String(50), index=True)
    par = Column(Integer, index=True)
    zip_code = Column(Integer)
    rounds = relationship("Round", back_populates="course")

class Round(Base):
    __tablename__ = "rounds"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    date = Column(Date)
    user = relationship("User", back_populates="rounds")
    course = relationship("Course", back_populates="rounds")
    scores = relationship("Score", back_populates="round")

class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True, index=True)
    round_id = Column(Integer, ForeignKey('rounds.id'))
    hole_number = Column(Integer, index=True)
    score = Column(Integer, index=True)
    round = relationship("Round", back_populates="scores")
