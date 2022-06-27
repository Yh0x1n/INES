#Module for Majors and Subjects
from pydantic import BaseModel
from users import *

class Majors(BaseModel):
    code : str
    name : str

class Subjects(BaseModel):
    code : str
    name : str
    teacher_ID = Teachers.id
    major_code = str