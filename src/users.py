# Module for users
from fastapi import APIRouter
from pydantic import BaseModel
import mariadb
import random

class id_generator():
    numbers = '1234567890'
    len = 4
    gen_id = ''.join(random.sample(numbers, len))

class userAuth(BaseModel):
    email : str
    password : str

class Contracts(BaseModel):
    id = id_generator.gen_id
    contract_type : str

class Teachers(BaseModel):
    id = id_generator.gen_id
    userID : str
    contract : str

class Majors(BaseModel):
    code : str
    name : str

class Subjects(BaseModel):
    code : str
    name : str
    teacher_ID = int
    major_code = str

class Evaluators(BaseModel):
    id = id_generator.gen_id
    userID : str
    is_coordinator : bool
    major_code = str

class Instruments(BaseModel):
    id : int
    questions : str

class Users():
    """docstring for Users"""
    def __init__(self, db_cursors):
        self.cur = db_cursors

    def insert(self, new_user):
        try:
            self.cur.execute('''INSERT INTO usuarios (
                id, nombre, nombre2,nombre3,
                apellido, apellido2, apellido3,
                correo, contrasenna, cedula, es_admin
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?)''', (
                    new_user.id, 
                    new_user.name, 
                    new_user.name2, 
                    new_user.name3, 
                    new_user.lastname, 
                    new_user.lastname2, 
                    new_user.lastname3,
                    new_user.email, 
                    new_user.password, 
                    new_user.cedula,
                    new_user.is_admin)
                    )
        except mariadb.Error as e:
            print (f'[!] Error inserting into table "usuarios": {e}')
            return False

        return True

    def delete(self, id):
        print(f'[!database] Deleting a user with id: {id}')
        try:
            # WARING: update to prevent SQL injection atacks
            res = self.cur.execute(f'DELETE FROM usuarios WHERE ID={id};')


        except mariadb.Error as e:
            print (f'[!] Error deleting from table "usuarios": {e}')
            return False

        return True

    #TO-DO: Finish later
    def get(self, value, by="id"): 
        """Function to get user by it's ID, and 
        shows name and last name"""
        print (f"[!] Finding user by {by}: {value}")
        try:
            #TO-DO: Change for a match
            if by == 'id':
                self.cur.execute(f"select * from usuarios where ID = {id}")
            elif by == 'email':
                self.cur.execute(f'select * from usuarios where correo = "{value}"')
            
            tuple_user = self.cur.fetchall()[0]
            
            print(f'the tuple_user is: {tuple_user}')

            user = {
                'id': tuple_user[0],
                'email': tuple_user[1],
                'password': tuple_user[2],
                'name' : tuple_user[2],
                'lastname' : tuple_user[5]
            }

            return user

        except mariadb.Error as e:
            print ("[Error] There was an error during this action.")
            print (e)
            return {}

    #Function to modify user based on different conditions (still on test phase)
    def mod_user(self, name, name2, name3,
                lastname, lastname2, lastname3,
                email, cedula, id, password,):
        print ("[!] Modifying user...")
        try:
            self.cur.execute('select * from usuarios;')
            if name:
                self.cur.execute(f'update usuarios set nombre = "{name}" where ID = {id};')
            
            elif name2:
                self.cur.execute(f'update usuarios set nombre2 = "{name2}" where ID = {id};')
            
            elif name3:
                self.cur.execute(f'update usuarios set nombre3 = "{name3}" where ID = {id};')
            
            elif lastname:
                self.cur.execute(f'update usuarios set apellido = "{lastname}" where ID = {id};')
            
            elif lastname2:
                self.cur.execute(f'update usuarios set apellido2 = "{lastname2}" where ID = {id};')
            
            elif lastname3:
                self.cur.execute(f'update usuarios set apellido3 = "{lastname3}" where ID = {id};')
            
            elif email:
                self.cur.execute(f'update usuarios set correo = "{email}" where ID = {id};')

            elif cedula:
                self.cur.execute(f'update usuarios set cedula = {cedula} where ID = {id};')
            
            elif password:
                self.cur.execute(f'update usuarios set contrasenna = "{password}" where ID = {id};')
            
            
            #I want to do an elif where you can read two values at the same time as True

            return True     

        except mariadb.Error as e:
            return e