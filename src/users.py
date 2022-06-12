# Module for users
from fastapi import APIRouter
from pydantic import BaseModel
import random

user = APIRouter()

class token_generator():
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    Symbols = '¿?¡!$%&#-_+\/<ñ>'
    all = upper + lower + numbers + Symbols
    len = 10
    genToken = ''.join(random.sample(all, len))

class user_generator(): # Class for user ID generator
    numbers = '0123456789'
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    all = numbers + letters
    len = 8
    genID = ''.join(random.sample(all, len))

class userID(BaseModel, user_generator): # Class for username and ID parameters
    nick : str
    id = user_generator.genID

class userAuth(BaseModel):
    email: str
    password: str
    id = user_generator.genID
    nickname : str
    role : str
        

@user.get('/func/admin')
def admin():
    
    return "Use route has been gotten succesfully"

@user.get('/func/user_route')
def getUser():
    return "Use route has been gotten succesfully"

@user.get('/func/user_route')
def getUser():
    return "Use route has been gotten succesfully"

@user.get('/func/user_route')
def getUser():
    return "Use route has been gotten succesfully"