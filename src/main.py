#INES
#by Yhoxin Rossell, Hernán Guerrero and Douglas Socorro

from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.database import ines_db, mariadb
from src.users import *

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
    
@ines.put('/func/regist')
def regist_user(data: userAuth):
    res = ines_db.insert_user(data.id, data.nickname, data.email, data.password, data.role)
    return res

@ines.get('/func/show_user/{id}') #We need to fix this
def obtain_user():
    try:
        print ('[!] Getting user...')
        res = ines_db.get_user(id)
        return res
    
    except mariadb.Error as e:
        print ('[!] There was an error during this action.\n')
        return e

@ines.post('func/modify_user') #Function to modify user
def mod_user():
    return

@ines.delete('func/delete_user') #Function to delete user from the database
def del_user():
    return

@ines.post('/func/order_66')
def delete_ines_db():
    ines_db.drop_all()
    
    #Wipes away all the database >:)
    # This is pending to fix and improve
    