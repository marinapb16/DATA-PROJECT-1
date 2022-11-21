import psycopg2

from data import quiosco
quiosco.data_flores()

#conexión con postgres
conexion = psycopg2.connect(
    host='db',
    user='user',
    password='admin',
    database='postgres'
)
conexion.autocommit = True
cursor = conexion.cursor()

print('Conexión realizada con éxito')
#tabla = "CREATE TABLE flor (Nombre STRING(100) NOT NULL, Tipo STRING(100) NOT NULL);"
#cursor.execute(tabla)

#query = "INSERT INTO flor (Nombre, Tipo) VALUES ({response['name']}, {response['type']})"
#cursor.execute(query)
