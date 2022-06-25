import mariadb
import sys
from users import userAuth

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
                        'id bigint unsigned not null auto_increment primary key,'
                        'nom varchar (50) not null,'
                        'nom2 varchar (50) null,'
                        'nom3 varchar (50) null,'
                        'ap varchar (50) not null,'
                        'ap2 varchar (50) null,'
                        'ap3 varchar (50) null,'
                        'CI varchar (15) not null,'
                        'nac date not null,'
                        'nickname varchar (75) not null'
                        ');')

        self.cur.execute('create table if not exists users_role('
                        'nickname varchar (75) not null key,'
                        'email varchar (120) not null,'
                        'passw varchar (30) not null,'
                        'role varchar (20) not null'
                        ');')
        
    def insert_user (self, id, nickname, email, password,  role): #Function to insert an user in the database by email and password
        try:
            self.cur.execute(f'insert into users_role (id, nickname, email, passw, role) values ("{id}", "{nickname}", "{email}", "{password}", "{role}");')
            return True
        except mariadb.Error as e:
            print ("[Error] There was an error during this action.")
            print(e)
            return False
    
    def get_user(self, nickname, role): #Function to get user by its nickname and role
        print (f"[!] Finding user with the name {nickname}")
        try:
            res = self.cur.execute("select * from users_role where nickname = ", nickname," and role = ", role,";")
            print (f"[!] The user(s) is(are): {nickname}, {role}")
            return res.fetchall()[0]

        except mariadb.Error as e:
            print ("[Error] There was an unknown error during this action.")
            print (e)
            return False
    
    def drop_all (self):
        self.cur.execute ("drop table if exists users_data;")

ines_db = DB()