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

    return res