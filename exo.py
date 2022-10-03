import mysql.connector
mydb = mysql.connector.connect(host="localhost", username="root", password="")

print(mydb)

if(mydb):
    print("connexion succefful")
else:
    print("connexion failled")