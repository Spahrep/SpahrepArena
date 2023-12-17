# IMPORTS ETC
import mysql.connector
import hashlib
import auth
import newAccount

#define a global variable for debugging
debug_on = True

def debug(string):
    if(debug_on):
        print (string)
    else:
        pass
try:    
    from config import host, user, password, database

    mydb = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
        )

    mycursor = mydb.cursor()
except Exception as e:
    print("Error connecting to DB: "+e)
    
sqlString = ""
salt=""
userFound = False
userAuth = False
userID = None;

while userID == None:
    userSelection = input("Please Select a command from below\n1)Log in \n2)Create New Account\n3)Activate Account\n4)Quit\n").lower()
    if userSelection == "1":
        userID = auth.authUser(mydb)
    elif userSelection == "2":
        newAccount.createUser(mydb)
    elif userSelection == "3":
        newAccount.activateUser(mydb)
        continue
    elif userSelection == "4":
        break

print("Type /help for help")

while True:
    input("Choose an option:\n1)Go to the Arena\n2)Go to the Armoury\n3)Go to the Weapon Smith\n4)Craft\n5)Look in your Backpack")

mycursor.close()
mydb.close()
    
