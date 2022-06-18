#INES
#by Yhoxin Rossell, Hernán Guerrero and Douglas Socorro

from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from database import ines_db, mariadb
from users import *

'''MAIN APP SECTION'''
ines = FastAPI()

ines.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

'''USERS SECTION'''

def generate_token(x : token_generator): 
    token = x.gen_token
    return token

@ines.post("/auth")
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
    
@ines.put('/regist')
def regist_user(data: userAuth):
    '''Registers the user in the system and saves
        them into the database'''
    res = ines_db.insert_user(data.id, data.name, data.name2, data.lastname,
                        data.lastname2, data.email, data.password, data.cedula)
    return res

@ines.get('/user') #Function to get user from the database
def get_user(id : str):
    '''Obtains the user from the database'''
    print(f'[!] user id: {id}')
    try:
        print ('[!] Getting user...')
        res = ines_db.get_user(id)
        return res
    
    except mariadb.Error as e:
        print ('[!] There was an error during this action.\n')
        return e

@ines.post('/modify_user') #Function to modify user
def mod_user(id : int, name : str = None, name2 : str = None, lastname : str = None, lastname2 : str = None,
            email : str = None, cedula : int = None):
    '''Modifies the user in the database'''
    try:
        res = ines_db.mod_user(name, name2, lastname, lastname2, email, cedula, id)
        return res

    except mariadb.Error as e:
        print ('[!] There was an error during this action.\n')
        return e

@ines.delete('/delete_user') #Function to delete user from the database
def del_user(id : int):
    '''Deletes user from the database by its ID.'''
    try:
        res = ines_db.delete_user(id)
        return res
    except mariadb.Error as e:
        return e

'''FORMULARIES SECTION'''

@ines.get('/forms')
def get_form():
    return

@ines.post('/forms')
def post_form():
    return

@ines.delete('/forms-delete')
def del_form():
    return

'''DATABASE SECTION'''

@ines.post('/order_66')
def delete_ines_db():
    '''BE CAREFUL, this wipes away important parts of the database...
    like EVERYTHING ON IT.'''
    ines_db.drop_all()
    
    #Wipes away all the database >:)
    # This is pending to fix and improve