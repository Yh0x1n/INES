#INES
#by Yhoxin Rossell, Hernán Guerrero and Douglas Socorro

from fastapi import FastAPI
import random


mainsite = FastAPI()

@mainsite.get("/")

def testmsg():
    return "Hello! This is the first step of project INES. ^^"