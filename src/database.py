# Module for database using MariaDB

import mariadb
import sys
from users import Users
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
        self.users = Users(self.cur)
        self.forms = Forms(self.cur)
        

        #Ensure the DB
        self.cur.execute('create database if not exists ines_db;')
        self.cur.execute('use ines_db;')    
        
        #Creating DB tables by SQL commands, in case they don't exist
        self.cur.execute('CREATE TABLE if NOT EXISTS usuarios ('
                        'ID INT (10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                        'correo VARCHAR(50) NOT NULL UNIQUE,'
                        'contrasenna VARCHAR (50) NOT NULL,'
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