#INES
#by Yhoxin Rossell, Hernán Guerrero and Douglas Socorro

from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database import db
import users

# Main app section
mainsite = FastAPI()
mainsite.include_router(users)
mainsite.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

def exists_user(email):
    if(user := db.get_user(email)):
        return True
        
    return False

@mainsite.post("/func/auth")
def auth(data: users.userAuth):
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
    
@mainsite.put('/func/regist')
def regist_user(data: users.userAuth):
    res = db.regist_user(data.email, data.password)

    return {
        'success': res
    }

@mainsite.put('/func/modify')
def modify_user(data: users.userAuth.userData):
    mod = db.modify_user(data.em, data.word)
    try:
        return {
            'sucess' : mod
        }
    except:
        return "Could not modify user"
    

@mainsite.post('/func/order_66')
def delete_db():
    db.drop_all()
    
    #This is pending to fix and improve
    