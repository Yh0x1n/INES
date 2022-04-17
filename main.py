#INES
#by Yhoxin Rossell, Hernán Guerrero and Douglas Socorro

from pydantic import BaseModel
from fastapi import FastAPI
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
    
# Main app section
mainsite = FastAPI()

@mainsite.get("/") # Test message
def testmsg():
    return "Hello! This is the first step for project INES. ^^"

@mainsite.post("/users-ID") # Response body for username and ID
def usuario(userid: userID):
    return f"Hello, {userid.nick}! your user ID is {userid.id}."