import requests
import json
import psycopg2

def data_flores():
 url = 'https://geoportal.valencia.es/apps/OpenData/UrbanismoEInfraestructuras/OCO_KIOSCOS_FLORES.json'
 r = requests.get(url)
 response = r.json()
 datos: str = response
 return response
 
#Map json fields
response = data_flores()


#conexión con postgres
'''conexion = psycopg2.connect(
    host='localhost',
    user='user',
    password='admin',
    database='flores'
)
conexion.autocommit = True
cursor = conexion.cursor()

tabla = "CREATE TABLE flor (Nombre NOT NULL, Tipo NOT NULL);"
cursor.execute(tabla)

query = "INSERT INTO flor (Nombre, Tipo) VALUES ('{response['name']}', '{response['type']}')"
cursor.execute(query)
'''



