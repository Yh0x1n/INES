from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel

from database import ines_db

import random
import util

from users import userAuth

router = APIRouter()

@router.post("/auth")
def auth(data: userAuth):
    """Verify user email and password, 
    if both are valid, return a random token"""
    print(f'[!] Authenticating user with: {data}')
    try:
        user = ines_db.users.get(data.email, by='email')
        print({ 'auth': data, 'user': user})

        if data.password == user['password']:
            # the email and password are valid
            token = util.token_generator()
            return { 'success': True, 'user': user, 'token': token }

        return { 'success': False, 'err': 'password' }
    except KeyError:
        return { 'success': False, 'err': 'email' }    

    return res
