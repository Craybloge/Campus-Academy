import mysql.connector
from mysql.connector import errorcode
from constantes import CONFIG
from pokemon import Pokemon

try:
  db = mysql.connector.connect(**CONFIG)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    cursor = db.cursor()
    
    table = Pokemon(cursor)
    table.print_all()
    db.close()



      
