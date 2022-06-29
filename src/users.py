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
    def __init__(self, db_cursor):
        self.cur = db_cursor

    def insert(self, new_user):
        try:
            self.cur.execute('''INSERT INTO usuarios (
                id, nombre, nombre2,nombre3,
                apellido, apellido2, apellido3,
                correo, contrasenna, cedula, nacimiento, es_admin
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', (
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
                    new_user.bday,
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
    def get(self, value, by = "id"): 
        """Function to get user by it's ID, and 
        shows name and last name"""
        print (f"[!] Finding user by {by}: {value}")
        try:
            #TO-DO: Change for a match
            if by == 'id':
                self.cur.execute(f"select * from usuarios where ID = {value}")
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
    def mod_user(self, id, new_data):
        print (f"[!] Modifying user by ID: {id}")
        try:
            self.cur.execute('select * from usuarios;')
            if new_data.name:
                self.cur.execute(f'update usuarios set nombre = "{new_data.name}" where ID = {id};')
            
            elif new_data.name2:
                self.cur.execute(f'update usuarios set nombre2 = "{new_data.name2}" where ID = {id};')
            
            elif new_data.name3:
                self.cur.execute(f'update usuarios set nombre3 = "{new_data.name3}" where ID = {id};')
            
            elif new_data.lastname:
                self.cur.execute(f'update usuarios set apellido = "{new_data.lastname}" where ID = {id};')
            
            elif new_data.lastname2:
                self.cur.execute(f'update usuarios set apellido2 = "{new_data.lastname2}" where ID = {id};')
            
            elif new_data.lastname3:
                self.cur.execute(f'update usuarios set apellido3 = "{new_data.lastname3}" where ID = {id};')
            
            elif new_data.email:
                self.cur.execute(f'update usuarios set correo = "{new_data.email}" where ID = {id};')

            elif new_data.cedula:
                self.cur.execute(f'update usuarios set cedula = {new_data.cedula} where ID = {id};')
            
            elif new_data.password:
                self.cur.execute(f'update usuarios set contrasenna = "{new_data.password}" where ID = {id};')
            
            
            #I want to do an elif where you can read two values at the same time as True

            return True     

        except mariadb.Error as e:
            return e