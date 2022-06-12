import mariadb
import sys
from src.users import userAuth

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
        self.cur.execute('CREATE TABLE if NOT EXISTS users_data ('
                        'id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                        'nom VARCHAR (50) NOT NULL,'
                        'nom2 VARCHAR (50) NULL,'
                        'nom3 VARCHAR (50) NULL,'
                        'ap VARCHAR (50) NOT NULL,'
                        'ap2 VARCHAR (50) NULL,'
                        'ap3 VARCHAR (50) NULL,'
                        'CI VARCHAR (15) NOT NULL,'
                        'nac date NOT NULL,'
                        'nickname VARCHAR (75) NOT NULL'
                        ');')

        self.cur.execute('CREATE TABLE if NOT EXISTS users_role('
                        'nickname VARCHAR (75) NOT NULL KEY,'
                        'email VARCHAR (120) NOT NULL,'
                        'passw VARCHAR (30) NOT NULL,'
                        'role VARCHAR (20) NOT NULL'
                        ');')
        
    def insert_user (self, id, nickname, email, password,  role): #Function to insert an user in the database by email and password
        try:
            self.cur.execute(f'insert into users_role (id, nickname, email, passw, role) values ("{id}", "{nickname}", "{email}", "{password}", "{role}");')
            return True
        except mariadb.Error as e:
            print ("[Error] There was an error during this action.")
            print(e)
            return False
    
    def get_user(self, id, nickname, role): #Function to get user by it's ID, and shows nickame and role
        print (f"[!] Finding user with the ID {id}")
        try:
            res = self.cur.execute(f"select * from users_role where ID = {id}")
            res.fetchall()[0]
            return {nickname : role}

        except mariadb.Error as e:
            print ("[Error] There was an unknown error during this action.")
            print (e)
            return False
    
    def drop_all (self):
        self.cur.execute ("drop table if exists users_data;")

ines_db = DB()