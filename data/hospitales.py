import requests
import json
import psycopg2

#def data_flores():
url = 'https://valencia.opendatasoft.com/explore/dataset/hospitales/download/?format=json&timezone=Europe/Berlin&lang=es'
r = requests.get(url)
datos = r.json()

distrito = datos[2]['coddistrit']
geo = datos[2]['geo_point_2d']
nombre = datos[2]['nombre']
print(distrito)
print(geo)
print(nombre)
 #return response
 

#Map json fields
#response = data_flores()