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

    def __init__(self):
        self.id = id_generator.gen_id
        self.name : str
        self.name2 : str
        self.name3 : str
        self.lastname : str
        self.lastname2 : str
        self.lastname3 :str
        self.email : str
        self.password : str
        self.cedula : int
        