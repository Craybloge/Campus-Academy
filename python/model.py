
import mysql.connector
from mysql.connector import errorcode
from constantes import CONFIG

class Model():

    def __init__(self):
        self.nom = None
        self.attributs = None
