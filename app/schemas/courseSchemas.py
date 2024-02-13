from pydantic import BaseModel

class CourseBase(BaseModel):
    name: str
    city: str
    state: str
    par: int
    zip_code: int

class CourseCreate(BaseModel):
    name: str
    city: str
    state: str
    par: int
    zip_code: int

class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True