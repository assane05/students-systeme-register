import mysql.connector
mydb = mysql.connector.connect(host="localhost", username="root", password="", database="projetpython")

mycursor = mydb.cursor()
mycursor.execute("Create table etudiants(firs_name varchar(200), last_name varchar(200), telephone int(16), city varchar(100), genre varchar(10) )")