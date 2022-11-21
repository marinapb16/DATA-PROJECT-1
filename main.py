import psycopg2

from data import quiosco
quiosco.data_flores()

#conexión con postgres
conexion = psycopg2.connect(
    host='localhost',
    user='user',
    password='admin',
    database='postgres'
)
conexion.autocommit = True
cursor = conexion.cursor()

tabla = "CREATE TABLE flor (Nombre NOT NULL, Tipo NOT NULL);"
cursor.execute(tabla)

query = "INSERT INTO flor (Nombre, Tipo) VALUES ('{response['name']}', '{response['type']}')"
cursor.execute(query)
