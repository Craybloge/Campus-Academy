
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
    def get_where_id(self, id):
        query = "  SELECT * FROM " + self.nom + " WHERE id" + self.nom + " = " + str(id)
        self.cursor.execute(query)
        return self.cursor
    def create(self, **kwargs):
        query = " INSERT INTO " + self.nom + " ("
        for i in self.attributs:
            query += i + ", "
        query = query[:-2] + ") VALUES ('"
        for i in self.attributs:
            query += kwargs[i] + "', '"
        query = query[:-3] + ");"
        self.cursor.execute(query)


    def update(self, id, **kwargs):
        query = "UPDATE " + self.nom + " SET "
        for i in kwargs:
            query += i + "='"+kwargs[i] + "', "
        query = query[:-2]
        query += " WHERE id" + self.nom + " = " + str(id)
        self.cursor.execute(query)
    def delete(self, id):
        query = "DELETE FROM " + self.nom + " WHERE id" + self.nom + " = " + str(id)
        self.cursor.execute(query)
    def print_all(self):
        to_print = self.get_all()
        for i in to_print:
            for j in i:
                print(str(j) + " | ", end="")
            print("")