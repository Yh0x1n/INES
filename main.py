#INES
#by Yhoxin Rossell, Hernán Guerrero and Douglas Socorro

from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import random

from database import db

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

class userEmail(BaseModel): #Test To-Do task from line 86
    email : str
    password : str
    
# Main app section
mainsite = FastAPI()

mainsite.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
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


dumbest_users = {
    'admin@gmail.com': { 
        "username": 'admin',
        "password": '1234567890'
    },
    'douglassocorro1@gmail.com': {
        "username": 'douglas',
        "password": 'onfire1234'
    },
}

def generate_token(): 
    token = 'some_random_token_12345'
    return token

class Auth(BaseModel):
    email: str
    password: str
    id = user_generator.user

def exists_user(email):
    if(user := db.get_user(email)): return True
        
    return False

@mainsite.post("/auth")
def auth(data: Auth):
    """Verify user email and password, 
    if both are valid, return a random token"""
    try:
        user = db.get_user(data.email)
        print({ 'auth': auth, 'user': user})
        # exists a user with that email

        if data.password == user['password']:
            # the email and password are valid
            token = generate_token()
            return { 'user': user, 'token': token }

        return { 'err': 'password' }
    except KeyError:
        return { 'err': 'email' }    
    
class User_register(BaseModel):
    email: str
    password: str
    
@mainsite.post('/regist')
def regist_user(data: User_register):
    res = db.regist_user(data.email, data.password)

    return {
        'success': res
    }


@mainsite.post('/order_66')
def delete_db():
    db.drop_all()
    
    #This is pending to fix and improve
    