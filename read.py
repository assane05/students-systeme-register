from unittest import result
import mysql.connector
mydb = mysql.connector.connect(host="localhost", username="root", password="", database="projetpython")

mycursor = mydb.cursor()
mycursor.execute("Select * from etudiants")

result = mycursor.fetchall()

for row in result:
    print(row) 