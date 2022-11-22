import requests
import json
import psycopg2

def data_colegios():

    url = 'https://valencia.opendatasoft.com/explore/dataset/centros-educativos-en-valencia/download/?format=json&timezone=Europe/Berlin&lang=es'
    r = requests.get(url)
    datos = r.json()

    conexion = psycopg2.connect(
    host='localhost',
    user='user',
    password='admin',
    database='postgres'
    )
    #conexion.autocommit = True
    cursor = conexion.cursor()

    name_Table = "colegios"

    # Create table statement
    sqlCreateTable = "create table "+name_Table+" (CodigoPostal INT, Nombre varchar(100));"

    # Create a table in PostgreSQL database

    cursor.execute(sqlCreateTable)
    conexion.commit()


    for i in range(len(datos)):
        query = "INSERT INTO hospitales (Distrito, Nombre) VALUES (%s, %s);"
        variables = [datos[i]['fields']['codpos'], datos[i]['fields']['dlibre']]
        cursor.execute(query,variables)
        conexion.commit()

data_colegios()


     



