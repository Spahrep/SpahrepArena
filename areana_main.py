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
    command = input("Command:").lower()

    if(command == "/help"):
        print("This is the help file....")
    elif(command == "quit"):
        quit
    else:
        ("Please type a valid command or type /help")
    

mycursor.close()
mydb.close()
    
