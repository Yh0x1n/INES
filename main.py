#INES
#by Yhoxin Rossell, Hernán Guerrero and Douglas Socorro

from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from config.database import ines_db
from routes.users import user

# Main app section
ines = FastAPI()
ines.include_router(user)
ines.add_middleware(
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
    if(user := ines_db.get_user(email)):
        return True
        
    return False

@ines.post("/func/auth")
def auth(data: user.userAuth):
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
def regist_user(data: user.userAuth):
    res = ines_db.regist_user(data.email, data.password)

    return {
        'success': res
    }
    

@ines.post('/func/order_66')
def delete_ines_db():
    ines_db.drop_all()
    
    #Wipes away all the database >:)
    # This is pending to fix and improve
    