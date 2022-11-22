import requests
import json
import psycopg2

def data_hospitales():

    url = 'https://valencia.opendatasoft.com/explore/dataset/hospitales/download/?format=json&timezone=Europe/Berlin&lang=es'
    r = requests.get(url)
    datos = r.json()

    #return response

    conexion = psycopg2.connect(
    host='localhost',
    user='user',
    password='admin',
    database='postgres'
    )
    #conexion.autocommit = True
    cursor = conexion.cursor()

    name_Table = "hospitales"

    # Create table statement
    sqlCreateTable = "create table "+name_Table+" (Distrito INT, Nombre varchar(100));"

    # Create a table in PostgreSQL database

    cursor.execute(sqlCreateTable)
    conexion.commit()


    for i in range(len(datos)):
        query = "INSERT INTO hospitales (Distrito, Nombre) VALUES (%s, %s);"
        variables = [datos[i]['fields']['coddistrit'], datos[i]['fields']['nombre']]
        cursor.execute(query,variables)
        conexion.commit()

data_hospitales()

    

