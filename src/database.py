# Module for database using MariaDB

import mariadb
import sys
from users import *
from forms import Forms

import config

print ("[!] Starting Database...")
class DB:

    '''CONNECTION TO THE DATABASE SECTION'''

    def __init__(self):
        #Connecting to the database
        try:
            conn = mariadb.connect(
            user = config.DB_USER,
            password = config.DB_PASSWORD,
            host = "127.0.0.1",
            port = 3306,
            )
            conn.autocommit = True
            
            print ("[!] Database successfully loaded!")

        except mariadb.Error as e:
            print (f"[!] Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        
        #Get cursor
        self.cur = conn.cursor()
        self.forms = Forms(self.cur)
        

        #Ensure the DB
        self.cur.execute('create database if not exists ines_db;')
        self.cur.execute('use ines_db;')    
        
        #Creating DB tables by SQL commands, in case they don't exist
        self.cur.execute('CREATE TABLE if NOT EXISTS usuarios ('
                        'ID INT (10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                        'correo VARCHAR(50) NOT NULL,'
                        'nombre VARCHAR (50) NOT NULL,'
                        'nombre2 VARCHAR (50) NULL,'
                        'nombre3 VARCHAR (50) NULL,'
                        'apellido VARCHAR (50) NOT NULL,'
                        'apellido2 VARCHAR (50) NULL,'
                        'apellido3 VARCHAR (50) NULL,'
                        'cedula VARCHAR (15) NOT NULL,'
                        'nacimiento DATE NOT NULL NULL,'
                        'es_admin BINARY (1) NOT NULL'
                        ');')

        self.cur.execute('CREATE TABLE if NOT EXISTS instrumentos ('
                        'ID INT(10) UNSIGNED NOT NULL PRIMARY KEY,'
                        'nombre VARCHAR(30) NOT NULL,'
                        'preguntas JSON NULL'
                        ');')
        
        self.cur.execute('CREATE TABLE if NOT EXISTS carreras('
                        'codigo VARCHAR (10) NOT NULL PRIMARY KEY,'
                        'nombre VARCHAR (30) NOT NULL'
                        ');')

        self.cur.execute('CREATE TABLE if NOT EXISTS tipos_de_contrato('
                        'ID INT (10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                        'tipo VARCHAR (20) NOT NULL'
                        ');')
        
        self.cur.execute('CREATE TABLE if NOT EXISTS evaluadores ('
                        'ID INT (10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                        'es_coordinador BINARY (1) NOT NULL,'
                        'carreras_codigo VARCHAR (10) NOT NULL,'
                        'usuarios_ID INT (10) UNSIGNED NOT NULL'
                        ');')
        
        self.cur.execute('CREATE TABLE if NOT EXISTS profesores ('
                        'ID INT (10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                        'usuarios_ID INT (10) UNSIGNED NOT NULL,'
                        'tipos_de_contrato_ID INT (10) UNSIGNED NOT NULL'
                        ');')

        self.cur.execute('CREATE TABLE if NOT EXISTS evaluaciones('
                        'ID INT (10) UNSIGNED NOT NULL PRIMARY KEY,'
                        'resultados JSON NULL,'
                        'fecha DATE NULL,'
                        'tipo INT (10) UNSIGNED NOT NULL,'
                        'instrumentos_ID INT (10) UNSIGNED NOT NULL,'
                        'profesores_ID INT (10) UNSIGNED NOT NULL,'
                        'evaluadores_ID INT (10) UNSIGNED NOT NULL'
                        ');')

        self.cur.execute('CREATE TABLE if NOT EXISTS materias('
                        'codigo VARCHAR (20) NOT NULL PRIMARY KEY,'
                        'nombre VARCHAR (45) NOT NULL,'
                        'profesores_ID INT (10) UNSIGNED NOT NULL,'
                        'carreras_codigo VARCHAR (10) NOT NULL'
                        ');')

        self.cur.execute('CREATE TABLE if NOT EXISTS horarios('
                        'ID INT (10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                        'modulo CHAR (50) NULL,'
                        'dia VARCHAR (20) NULL,'
                        'hora_inicio TIME NOT NULL,'
                        'hora_final TIME NOT NULL,'
                        'materias_codigo VARCHAR (45)'
                        ');')


    '''USERS SECTION'''

    #Function to insert an user in the database by email and password
    def insert_user (self, id, name, name2, lastname, lastname2, email, password, cedula):
        try:
            self.cur.execute(f'insert into usuarios (id, nombre, nombre2, apellido,'
                            f'apellido2, correo, contraseña, cedula) values'
                            f'("{id}", "{name}", "{name2}", "{lastname}", "{lastname2}", '
                            f'"{email}", "{password}", "{cedula}");')
            return f'The registed user is: {name}, {lastname}; ID: {id}'
        except mariadb.Error as e:
            print ("[Error] There was an error during this action.")
            print(e)
            return False

        return True

    #Function to get user by it's ID, and shows name and last name
    def get_user(self, id): 
        print (f"[!] Finding user with the ID {id}")
        try:
            self.cur.execute(f"select * from usuarios where ID = {id}")
            user = self.cur.fetchall()[0]
            users_dict = {'name' : user[2], 'lastname' : user[5], 'id' : id}

            print (users_dict)
            return f"The user is: {user[2]} {user[5]}; ID: {id}"

        except mariadb.Error as e:
            print ("[Error] There was an error during this action.")
            print (e)
            return False
    
    #Function to delete user by its ID
    def delete_user(self, id):
        print("[!] Deleting user...")
        try:
            self.cur.execute("select * from usuarios;")
            print(f'data: {id}')
            self.cur.execute(f"delete from usuarios where ID = {id};")
            return True 
        
        except mariadb.Error as e:
            print ("[!] There was an error during this action.")
            return e

    #Function to modify user based on different conditions (still on test phase)
    def mod_user(self, name, name2, lastname, lastname2, email, cedula, id):
        print ("[!] Modifying user...")
        try:
            self.cur.execute('select * from usuarios;')
            if name:
                self.cur.execute(f'update usuarios set nombre = "{name}" where ID = {id};')
            
            elif name2:
                self.cur.execute(f'update usuarios set nombre2 = "{name2}" where ID = {id};')
            
            elif lastname:
                self.cur.execute(f'update usuarios set apellido = "{lastname}" where ID = {id};')
            
            elif lastname2:
                self.cur.execute(f'update usuarios set apellido2 = "{lastname2}" where ID = {id};')
            
            elif email:
                self.cur.execute(f'update usuarios set correo = "{email}" where ID = {id};')

            elif cedula:
                self.cur.execute(f'update usuarios set cedula = {cedula} where ID = {id};')
            
            #I want to do an elif where you can read two values at the same time as True

            return True     

        except mariadb.Error as e:
            return e

    '''FORMS SECTION'''

    def create_form():

        return

    def get_form(self, id):
        try:
            self.forms.execute(f'select * from instrumentos where ID = {id};')
        
            return True

        except mariadb.Error as e:
            print('[!] There was an error during this action.')
            return e

    def del_form(self, id):

        return
    #Function to insert a major given in college. Still on idea phase      
    '''def insert_major(self):
        return False'''

    #Function to drop a table from the database
    def drop_all (self):
        try:
            res = self.cur.execute ("drop table if exists usuarios;")
            return res
        except mariadb.Error as e:
            print ("There was an error during this action...")
            return e

ines_db = DB()