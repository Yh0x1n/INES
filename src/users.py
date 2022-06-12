# Module for users
from tarfile import LENGTH_LINK
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

class user_generator(): # Class for user ID generator
    numbers = '1234567890'
    i = 0
    len = 8
    genID = ''.join(random.sample(numbers, len))

class userID(BaseModel): # Class for username and ID parameters
    nick : str
    id = user_generator.genID

class userAuth(BaseModel):
    id = user_generator.genID
    nickname : str
    email : str
    password : str
    role : str