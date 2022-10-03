import mysql.connector
mydb = mysql.connector.connect(host="localhost", username="root", password="", database="projetpython")

mycursor = mydb.cursor()

sql = "DELETE from etudiants WHERE firs_name='pap' "

mycursor.execute(sql)

mydb.commit()