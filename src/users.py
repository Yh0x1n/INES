# Module for users
from fastapi import APIRouter
from pydantic import BaseModel
import random

class token_generator():
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    Symbols = '¿?¡!$%&#-_+\/<ñ>'
    all = upper + lower + numbers + Symbols
    len = 10
    genToken = ''.join(random.sample(all, len))

class id_generator():
    numbers = '1234567890'
    len = 4
    gen_id = ''.join(random.sample(numbers, len))

class userAuth(BaseModel):
    id = id_generator.gen_id
    name : str
    name2 : str
    lastname : str
    lastname2 : str
    email : str
    password : str
    cedula : int
    is_admin : bool

class Contracts(BaseModel):
    id = id_generator.gen_id
    contract_type : str

class Teachers(BaseModel):
    id = id_generator.gen_id
    userID : str
    contract : str

class Majors(BaseModel):
    code : str
    name : str

class Subjects(BaseModel):
    code : str
    name : str
    teacher_ID = int
    major_code = str

class Evaluators(BaseModel):
    id = id_generator.gen_id
    userID : str
    is_coordinator : bool
    major_code = str

class Instruments(BaseModel):
    id : int
    questions : str