import mysql.connector

database = mysql.connector.connect(
    host = 'localhost', 
    user = 'root',
    password = 'password123',
)

cursorObject = database.cursor()

sql = "CREATE DATABASE django_crm"
cursorObject.execute(sql)

print("all done!")