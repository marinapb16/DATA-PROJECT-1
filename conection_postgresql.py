import psycopg2

try:
    connection=psycopg2.connect(
        host='localhost',
        user='user',
        password='admin'
    )
    print("conexión exitosa")
except Exception as ex:
    print(ex)