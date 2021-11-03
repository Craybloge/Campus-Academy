
import mysql.connector
from mysql.connector import connect, errorcode
from constantes import CONFIG

class Model():

    def __init__(self, cursor):
        self.cursor = cursor
        self.nom = None
        self.attributs = None

    def get_all(self):

        query = "  SELECT * FROM " + self.nom
        self.cursor.execute(query)
        return self.cursor
    def get_where_id(self, *args):
        pass
    def create(self, *args):
        pass
    def update(self, id, *args):
        pass
    def delete(self, *args):
        pass
    def print_all(self):
        to_print = self.get_all()
        for i in to_print:
            for j in i:
                print(str(j) + " | ", end=" ")
            print("")