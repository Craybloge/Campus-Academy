import mysql.connector

config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'CA_pokemon_course',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()