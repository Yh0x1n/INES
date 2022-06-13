import mariadb
import sys
from users import *
print ("[!] Starting Database...")
class DB:
    def __init__(self):
        #Connecting to DB
        try:
            conn = mariadb.connect(
            user = "root",
            password = "28289663",
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

        #Ensure the DB
        self.cur.execute('create database if not exists ines_db;')
        self.cur.execute('use ines_db;')    
        
        #Creating DB tables in case they don't exist
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
                        'ID INT (10) UNSIGNED NOT NULL PRIMARY KEY,'
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

    #Function to insert an user in the database by email and password
    def insert_user (self, id, name, name2, lastname, lastname2, email, password, cedula):
        try:
            self.cur.execute(f'insert into usuarios (id, nombre, nombre2, apellido,'
                            f'apellido2, correo, contraseña, cedula) values'
                            f'("{id}", "{name}", "{name2}", "{lastname}", "{lastname2}", '
                            f'"{email}", "{password}", "{cedula}");')
            return True
        except mariadb.Error as e:
            print ("[Error] There was an error during this action.")
            print(e)
            return False

    #Function to get user by it's ID, and shows name and last name
    def get_user(self, id, name, lastname): 
        print (f"[!] Finding user with the ID {id}")
        try:
            res = self.cur.execute(f"select * from users_role where ID = {id}")
            res.fetchall()[0]
            return {name : lastname}

        except mariadb.Error as e:
            print ("[Error] There was an unknown error during this action.")
            print (e)
            return False
    
    def drop_all (self):
        self.cur.execute ("drop table if exists users_data;")

ines_db = DB()