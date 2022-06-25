#INES
#by Yhoxin Rossell, Hernán Guerrero and Douglas Socorro
import mariadb

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

import util
from database import ines_db

# ROUTERS 
from routers import auth, users, forms


'''MAIN APP SECTION'''
ines = FastAPI()

ines.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ines.include_router(auth.router)
ines.include_router(users.router)
ines.include_router(forms.router)

'''USERS SECTION'''

@ines.get('/say')
def say():
    return { 'msg': 'Hello world!'}

# USERS

    

'''DATABASE SECTION'''

@ines.post('/order_66')
def delete_ines_db():
    '''BE CAREFUL, this wipes away important parts of the database...
    like EVERYTHING ON IT.'''
    ines_db.drop_all()
    
    #Wipes away all the database >:)
    # This is pending to fix and improve