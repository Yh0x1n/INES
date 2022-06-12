#INES
#by Yhoxin Rossell, Hernán Guerrero and Douglas Socorro

from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database import ines_db, mariadb
from users import *

# Main app section
ines = FastAPI()

ines.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def generate_token(x : token_generator): 
    token = x.gen_token
    return token

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
    res = ines_db.insert_user(data.id, data.name, data.name2, data.lastname, data.lastname2, data.email, data.password, data.cedula)
    return res

@ines.get('/func/show_user/{id}') #We need to fix this
def obtain_user(data: userAuth):
    try:
        print ('[!] Getting user...')
        res = ines_db.get_user(data.id, data.name, data.lastname)
        return res
    
    except mariadb.Error as e:
        print ('[!] There was an error during this action.\n')
        return e

@ines.post('func/modify_user') #Function to modify user
def mod_user():
    return

@ines.delete('/func/delete_user') #Function to delete user from the database
def del_user(data : userAuth):
    try:
        res = ines_db.delete_user(data.id)
        return res
    except mariadb.Error as e:
        return e

@ines.post('/func/order_66')
def delete_ines_db():
    ines_db.drop_all()
    
    #Wipes away all the database >:)
    # This is pending to fix and improve
    