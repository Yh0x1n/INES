import mariadb
import sys

print('starting database...')

class DataBase:
  def __init__(self):
    conn = self.get_connection();
    self.cur = conn.cursor()

    # ensure the database
    self.cur.execute('create database if not exists ines_test')
    self.cur.execute('use ines_test')

    # create database if not exists ines_test
    self.cur.execute('create table if not exists users (id int primary key not null auto_increment, email varchar(45) not null UNIQUE, password varchar(45) not null)')

  def regist_user(self, email, password):
    try:
      self.cur.execute('insert into users (email, password) values (?, ?)', (email, password))
      return True
    except mariadb.Error as err:

      print('hubo un error:')
      print(err)
      return False
    
  def get_user(self, email):
    print(f'finding user with email {email}')
    # Error de sintaxis serca del caracter "?"
    res = self.cur.execute("SELECT * FROM users WHERE email=?", email)
    print(f'users are: {res}')
    return res.fetchall()[0]


  def get_connection(self):
    try:
      conn = mariadb.connect(
          user="root",
          password="28289663",
          host="localhost",
          port=3306

      )
      conn.autocommit = True
    except mariadb.Error as e:
      print(f"Error connecting to MariaDB Platform: {e}")
      sys.exit(1)

    return conn

    def drop_all(self):
      self.cur.execute('drop table if exists users')

  
db = DataBase()
db.regist_user('mandarina_acida@gmail.com', '12345')

print('here you have the database.')
#conn.commit()

