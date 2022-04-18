#INES
#by Yhoxin Rossell, Hernán Guerrero and Douglas Socorro

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

mainsite.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@mainsite.get("/") # Test message
def testmsg():
    return "Hello! This is the first step for project INES. ^^"

@mainsite.post("/users-ID") # Response body for username and ID
def usuario(userid: userID):
    return f"Hello, {userid.nick}! your user ID is {userid.id}."


# define a path with post to verify user email and password

dubbest_users = [
    { 
        "username": 'admin',
        "email": 'admin@gmail.com',
        "password": '1234567890'
    },
    {
        "username": "douglas",
        "email": "douglassocorro1@gmail.com",
        "password": 'onfire1234'
    }
]

@mainsite.post("/auth")
def auth(email:str, password:str):
    for data in dubbest_users:
        if data.email == email:
            # existe un usuario con ese email
            if data.password == password:
                # el email y contraseña coinciden
                token = generate_token()
                return { 'token': token }

            return { 'err': 'password' }
        return { 'err': 'email' }

@mainsite.get('/exp')
def exp():
    return { 'msg': 'hello world!' }

# define a path with post to regist a user with email and password
