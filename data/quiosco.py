import requests
import json

def data_flores():
 url = 'https://geoportal.valencia.es/apps/OpenData/UrbanismoEInfraestructuras/OCO_KIOSCOS_FLORES.json'
 r = requests.get(url)
 response = r.json()
 datos: str = response
 return response
 
#Map json fields
response = data_flores()

#Conn a postgres
query = f"INSERT INTO test (coordenadas, emplazamiento) VALUES ('{response['name']}', '{response['name']}')"
print(query)



