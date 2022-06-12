#INES
#by Yhoxin Rossell, Hernán Guerrero and Douglas Socorro

from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database import ines_db, mariadb
from users import userAuth, token_generator

# Main app section
ines = FastAPI()

ines.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

'''dumbest_users = {
    'admin@gmail.com': { 
        "username": 'admin',
        "password": '1234567890'
    },
    'douglassocorro1@gmail.com': {
        "username": 'douglas',
        "password": 'onfire1234'
    },
}'''

def generate_token(): 
    token = token_generator.genToken
    return token

def exists_user(email):
    if(user := ines_db.get_user(email)):
        return True
        
    return False

@ines.post("/func/auth")
def auth(data: userAuth):
    """Verify user email and password, 
    if both are valid, return a random token"""
    try:
        user = ines_db.get_user(data.email)
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
    
@ines.post('/func/regist')
def regist_user(data: userAuth):
    res = ines_db.insert_user(data.id, data.email, data.password, data.nickname, data.role)
    return res
@ines.get('/func/show')
def obtain_user(data: userAuth):
    try:
        print ('[!] Getting user...')
        res = ines_db.get_user(data.nickname, data.role)
        return res
    
    except mariadb.Error as e:
        print ('[!] There was an error during this action.\n')
        return e
@ines.post('/func/order_66')
def delete_ines_db():
    ines_db.drop_all()
    
    #Wipes away all the database >:)
    # This is pending to fix and improve
    