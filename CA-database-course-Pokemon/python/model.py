
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
            query += str(kwargs[i]) + "', '"
        query = query[:-3] + ");"
        self.cursor.execute(query)

    def update(self, id, **kwargs):
        query = "UPDATE " + self.nom + " SET "
        for i in kwargs:
            query += i + "='"+ str(kwargs[i]) + "', "
        query = query[:-2]
        query += " WHERE id" + self.nom + " = " + str(id)
        self.cursor.execute(query)
    
    def delete(self, id):
        query = "DELETE FROM " + self.nom + " WHERE id" + self.nom + " = " + str(id)
        self.cursor.execute(query)

    def print_all(self):
        to_print = self.get_all()
        
        list_to_print = []
        compteur= 0
        for i in to_print:
            list_to_print.append([])
            for j in i:
                list_to_print[compteur].append(j)
            compteur += 1

        liste_nb_max = [0]*len(list_to_print[0])
        temp = [0]*len(list_to_print[0])
        for i in range(len(list_to_print)):
            for j in range(len(list_to_print[i])):
                temp[j] = len(str(list_to_print[i][j]))
                if temp[j] > liste_nb_max[j] :
                    liste_nb_max[j] = temp[j]

        for i in range(len(list_to_print)):
            print(" ")
            for j in range(len(list_to_print[i])):
                print(" ", list_to_print[i][j], " " *
                    (liste_nb_max[j] - len(str(list_to_print[i][j]))), "|", end="")
        print("")

    def delete_all(self):
        query = "DELETE FROM " + self.nom + " WHERE id" + self.nom + " > 0"
        self.cursor.execute(query)