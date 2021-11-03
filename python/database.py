import mysql.connector
from mysql.connector import errorcode
from constantes import CONFIG

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
    print("bonjour")
    query = "  SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='CA_pokemon_course' AND `TABLE_NAME`='pokemon'"
    cursor.execute(query)
    for i in cursor:
          print(i)

    db.close()



      
