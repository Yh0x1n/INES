import mariadb

class Forms:
    def __init__(self, cursor):
        self.cur = cursor
    
    def get(self, id):
        print(f'[!database] finding form with id: {id}')
        # WARING: update to prevent SQL injection atacks
        self.cur.execute(f'SELECT * FROM instrumentos WHERE ID = {id};')
        tuple_form = self.cur.fetchall()[0]
        #print(f'[!] the tuple_form is: {tuple_form}')

        form = {
            'id': tuple_form[0],
            'name': tuple_form[1],
            'items': tuple_form[2],
        }

        return form

    def insert(self, form):
        print(f'[!database] inserting form: {form}')
        try:
            self.cur.execute("""INSERT INTO instrumentos (
                ID, nombre, preguntas
            ) VALUES (?, ?, ?);""", (form.id, form.name, form.items))

        except mariadb.Error as e:
            print (f'[!] Error inserting into table "instrumentos": {e}')
            return False

        return True

    def delete(self, id):
        print(f'[!database] Deleting a form with id: {id}')
        try:
            # WARING: update to prevent SQL injection atacks
            res = self.cur.execute(f'DELETE FROM instrumentos WHERE ID={id};')


        except mariadb.Error as e:
            print (f'[!] Error deleting from table "instrumentos": {e}')
            return False

        return True