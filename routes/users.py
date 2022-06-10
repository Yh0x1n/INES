# Module for users
from fastapi import APIRouter
from pydantic import BaseModel
import random

class user_generator(): # Class for user ID generator
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    Symbols = '¿?¡!$%&#-_+\/<ñ>'
    all = upper + lower + numbers + Symbols
    len = 10
    user = ''.join(random.sample(all, len))

class userID(BaseModel, user_generator): # Class for username and ID parameters
    nick : str
    id = user_generator.user

class userAuth(BaseModel):
    email: str
    password: str
    id = user_generator.user

    def userData(userAuth):
        em = userAuth.email
        word = userAuth.password
        
user = APIRouter()
@user.get('/func/user_route')
def getUser():
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