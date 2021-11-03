import mysql.connector
from mysql.connector import errorcode
config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'CA_pokemon_course',
  'raise_on_warnings': True
}
print("bonjour")
try:
  db = mysql.connector.connect(**config)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = db.cursor()

  query = ("SELECT nom FROM Pokémons")
  cursor.execute(query)
  for i in cursor:
      print(i)

  print("au revoir")
  db.close()



  class CRUD():




    def __init__(self, nom):
      self.nom = nom





    def __repr__(self):
      return self.nom
    
    def CREATE(self , values):
      qry="INSERT INTO %s ( . , . , .) VALUES ('.',.,.);"

      