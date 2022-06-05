import mariadb
import sys

print('starting database...')

def get_db():
  try:
    conn = mariadb.connect(
        user="root",
        password="12345",
        host="localhost",
        port=3306

    )
    conn.autocommit = True
  except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

  cur = conn.cursor()
  # ensure the database
  cur.execute('create database if not exists ines_test')
    # create database if not exists ines_test
   # email and password
  cur.execute('use ines_test')
  cur.execute('create table if not exists users (id int primary key not null auto_increment, email varchar(45) not null, password varchar(45) not null)')
  cur.execute('insert into users (email, password) values (?, ?)', ('mandarina_acida@gmail.com', '12345'))

  print('here you have the database.')
  #conn.commit()

