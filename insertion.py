import mysql.connector
mydb = mysql.connector.connect(host="localhost", username="root", password="", database="projetpython")

mycursor = mydb.cursor()

sqlform = "Insert into etudiants(firs_name, last_name, telephone, city, genre) values(%s, %s, %s, %s, %s)"

inscrits = [("assane", "gueye", 770525909, "Dakar", "homme"), ("cheikh", "Pouye", 7705259, "Thies", "homme"),]

mycursor.executemany(sqlform, inscrits)

mydb.commit()