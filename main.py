#INES
#by Yhoxin Rossell, Hernán Guerrero and Douglas Socorro

from fastapi import FastAPI
from lib2to3.pygram import Symbols
import numbers, random

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
Symbols = '¿?¡!$%&#-_+-'
all = upper + lower + numbers + Symbols
len = 10
user = ''.join(random.sample(all, len))
nick = "random user"

    
mainsite = FastAPI()

@mainsite.get("/main")
def testmsg():
    return "Hello! This is the first step for project INES. ^^"

@mainsite.get("/users-ID")
def usuario():
    return f"Hello, {nick}! your user ID is {user}."
