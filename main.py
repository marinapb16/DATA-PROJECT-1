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
#conexion.autocommit = True
cursor = conexion.cursor()


#tabla = "CREATE TABLE flor (Nombre STRING(100) NOT NULL, Tipo STRING(100) NOT NULL);"
#cursor.execute(tabla)

#query = "INSERT INTO flor (Nombre, Tipo) VALUES ({response['name']}, {response['type']})"
#cursor.execute(query)
name_Table = "flor"


# Create table statement

sqlCreateTable = "create table "+name_Table+" (name varchar(128), type varchar(256));"

# Create a table in PostgreSQL database

cursor.execute(sqlCreateTable)
conexion.commit()


query = "INSERT INTO flor (name, type) VALUES (1,2)"

cursor.execute(query)
conexion.commit()

tables = cursor.fetchall()
for table in tables:

    print(table)