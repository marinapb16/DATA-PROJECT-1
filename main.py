import requests
import psycopg2
import random

#HOSPITALES

urlh = 'https://valencia.opendatasoft.com/explore/dataset/hospitales/download/?format=json&timezone=Europe/Berlin&lang=es'
r = requests.get(urlh)
datosh = r.json()

#return response

conexion = psycopg2.connect(
host='localhost',
user='user',
password='admin',
database='postgres'
)
#conexion.autocommit = True
cursor = conexion.cursor()

name_Tableh = "hospitales"

# Create table statement
sqlCreateTableh = "create table "+name_Tableh+" (CodigoPostal INT PRIMARY KEY, Nombre varchar(100));"

# Create a table in PostgreSQL database

cursor.execute(sqlCreateTableh)
conexion.commit()

listacodpos = [46001, 46002, 46003,	46004,	46005,	46006,	46007,	46008,	46009,	46010,	46011, 
46013, 46014,	46015,	46016,	46017,	46018,	46019,	46020,	46021,	46022,	46023,	46024,	
46025,	46026, 46035]

for i in range(len(datosh)):
    queryh = "INSERT INTO hospitales (CodigoPostal, Nombre) VALUES (%s, %s);"
    variablesh = [random.choice(listacodpos), datosh[i]['fields']['nombre']]
    cursor.execute(queryh,variablesh)
    conexion.commit()

#COLEGIOS
urlc = 'https://valencia.opendatasoft.com/explore/dataset/centros-educativos-en-valencia/download/?format=json&timezone=Europe/Berlin&lang=es'
r = requests.get(urlc)
datosc = r.json()

#return response

conexion = psycopg2.connect(
host='localhost',
user='user',
password='admin',
database='postgres'
)
#conexion.autocommit = True
cursor = conexion.cursor()

name_Tablec = "colegios"

# Create table statement
sqlCreateTablec = "create table "+name_Tablec+" (CodigoPostal INT, Nombre varchar(100));"

# Create a table in PostgreSQL database

cursor.execute(sqlCreateTablec)
conexion.commit()


#codigo = datosc[i]['fields']['codpos']
#if codigo in listacodpos:

for i in range(len(datosc)):
    queryc = "INSERT INTO colegios (CodigoPostal INT, Nombre) VALUES (%s, %s);"
    variablesc = [datosc[i]['fields']['codpos'], datosc[i]['fields']['dlibre']]
    cursor.execute(queryc,variablesc)
    conexion.commit()

#BARRIOS
conexion = psycopg2.connect(
host='localhost',
user='user',
password='admin',
database='postgres'
)
#conexion.autocommit = True
cursor = conexion.cursor()

name_Table = "barrios"

# Create table statement
sqlCreateTable = "create table "+name_Table+" (CodigoPostal INT, Nombre varchar(100));"

cursor.execute(sqlCreateTable)
conexion.commit()

query1 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46001, 'CiutatVella')"
cursor.execute(query1)
conexion.commit()

query2 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46002, 'CiutatVella')"
cursor.execute(query2)
conexion.commit()

query3 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46003, 'CiutatVella')"
cursor.execute(query3)
conexion.commit()

query4 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46004, 'Eixample')"
cursor.execute(query4)
conexion.commit()

query5 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46005, 'Eixample')"
cursor.execute(query5)
conexion.commit()

query6 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46006, 'Eixample')" 
cursor.execute(query6) 
conexion.commit() 

query7 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46007, 'Jesús')" 
cursor.execute(query7) 
conexion.commit() 

query8 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46008, 'Extramurs')"
cursor.execute(query8)
conexion.commit()

query9 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46009, 'La Saida')"
cursor.execute(query9)
conexion.commit()


query10 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46010, 'El pla del real')" 
cursor.execute(query10) 
conexion.commit() 

query11 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46011, 'Poblats Maritims')"
cursor.execute(query11)
conexion.commit()

query13 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46013, 'Quatre Carrers')"
cursor.execute(query13)
conexion.commit()

query14 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46014, 'Patraix')"
cursor.execute(query14)
conexion.commit()

query15 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46015, 'Campanar')"
cursor.execute(query15)
conexion.commit()

query16 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46016, 'PoblesNord')"
cursor.execute(query16)
conexion.commit()

query17 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46017, 'Jesus')"
cursor.execute(query17)
conexion.commit()

query18 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46018, 'Olivereta')"
cursor.execute(query18)
conexion.commit()

query19 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46019, 'Rascanya')"
cursor.execute(query19)
conexion.commit()
query20 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46020, 'Benimaclet')"
cursor.execute(query20)
conexion.commit()
query21 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46021, 'Algirós')"
cursor.execute(query21)
conexion.commit()
query22 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46022, 'Algirós')"
cursor.execute(query22)
conexion.commit()
query23 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46023, 'CaminsAlGrau')"
cursor.execute(query23)
conexion.commit()

query24 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46024, 'Poblats MArítims')"
cursor.execute(query24)
conexion.commit()

query25 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46025, 'Benicalap')"
cursor.execute(query25)
conexion.commit()

query26 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46026, 'Pobles Sud')"
cursor.execute(query26)
conexion.commit()

query35 = "INSERT INTO barrios (CodigoPostal, Nombre) VALUES (46035, 'Pobles Oest')"
cursor.execute(query35)
conexion.commit()