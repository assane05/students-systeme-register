import mysql.connector
mydb = mysql.connector.connect(host="localhost", username="root", password="", database="projetpython")

mycursor = mydb.cursor()

#sql = "UPDATE etudiants SET firs_name='demba' WHERE firs_name='assane' and last_name='gueye' and telephone=770525909 and city='Dakar' and genre='homme'"
sql = "UPDATE etudiants SET firs_name='pap' WHERE firs_name='demba' "
mycursor.execute(sql)

mydb.commit()