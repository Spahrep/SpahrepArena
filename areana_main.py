import mysql.connector
from config import host, user, password, database
print("hello")

mydb = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database
    )

mycursor = mydb.cursor()

mycursor.execute("Select * from test_table")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
##
    import mysql.connector

print("hello")
