import mysql.connector
import hashlib
import getpass
import passwordStr
import random
import string


#define a global variable for debugging
debug_on = True
def debug(string):
    if(debug_on):
        print (string)
    else:
        pass

def createUser(mydb):
    mycursor = mydb.cursor()
    firstName = None
    lastName = None
    userName = None
    email = None
    password = None
    passwordConfirm = None
    confirmCode = None
    userID = None
    

    isCorrect = False

    while not isCorrect:
        #ask for all their values
        userName = input("Please type your user name:")

## Check if the user name is already in the db
        debug("UserName:" + userName)
        mycursor.callproc(("CheckForUserName"),(userName,))
        # Fetch the results from the stored procedure
        results = mycursor.stored_results()
        result_set = next(results, None)  # Get the first result set

        if result_set is not None:
            rows = result_set.fetchall()
            if rows:
                print("This user name is already taken.")
                for row in rows:
                    print(row)  # This should print the userID if the procedure is called successfully
                continue
        else:
            debug("A-ok")
                
        
        firstName = input("Please type your first name:")
        lastName = input("Please type your last name:")
        email = input("Please type your email:")


## Check if the email is already in the db
        mycursor.callproc(("CheckForEmail"),(email,))
        # Fetch the results from the stored procedure
        results = mycursor.stored_results()
        result_set = next(results, None)  # Get the first result set

        if result_set is not None:
            rows = result_set.fetchall()
            if rows:
                print("This email is already in use.")
                for row in rows:
                    print(row)  # This should print the userID if the procedure is called successfully
                continue
        else:
            debug("A-ok")


        matching = False
        length = False
        print("Passwords must be at least 8 character, contain an upper and lower case letter, a digit and a symbol")
        while not matching :
            goodPass = False
            message = ""
            while not goodPass:
                password = getpass.getpass("Password:")
                goodPass = passwordStr.checkPass(password,message)
                    
            passwordConfirm = getpass.getpass("Please verify your password:")
            matching = password == passwordConfirm
            if(not matching):
                print("Passwords did not match")
            else:
                isCorrect = True

            
        #ask if everything is correct, if no, contine, if yes break.

    # Generate a random string of 10 letters
    salt = ''.join(random.choices(string.ascii_letters, k=10))
    debug(salt)
    
    password = salt + password
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode())
    hash_hex = sha256_hash.hexdigest()
    debug(hash_hex)

    createUserSP = "CreateUser"

    mycursor.callproc(createUserSP,(firstName,lastName,email,hash_hex,userName,salt))
    mydb.commit()
    
    return userID

def activateUser(mydb):
    userID = None
    mycursor = mydb.cursor()
    userName = input("User Name:")
    code = input("Activation Code:")
    code = code[:12]
    
    sqlString = "Select userID from user_table where userName = %s and isActivated = FALSE"
    mycursor.execute(sqlString,(userName,))
    myresult = mycursor.fetchall()
    if myresult:
            # Extract the userID from the first row
            userID = myresult[0][0]
            sqlString = "Update user_table set isActivated = TRUE where userID = %s and confirmCode = %s"
            mycursor.execute(sqlString,(userID,code))
            
            #procedureName = "ActivateUser"
           # mycursor = mydb.cursor()
            #test = mycursor.callproc(procedureName,(userID,code))
            #print(test)
            affectedRows = mycursor.rowcount
            mydb.commit()
            
            debug("ID Found, rowcount for activate: ")
            debug(affectedRows)
            if affectedRows == 0:
                print("Invalid User Name or Activation Code")
            else:
                print("User has been activated")
    else:
        print("Invalid User Name or Activation Code")
    
