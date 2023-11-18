# IMPORTS ETC
import mysql.connector
import hashlib

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
except Exceptoin as e:
    print("Error connecting to DB: "+e)
    
sqlString = ""
salt=""
userFound = False
userAuth = False
userID = 0;

while not userAuth:
    userName = input("Please type your user name:")
    password = input("Please type your password:")
    sqlString = "Select Salt from user_table where userName = %s and isActivated = TRUE"
    mycursor.execute(sqlString,(userName,))
    myresult = mycursor.fetchall()

    # Check if there is at least one result
    if myresult:
        # Extract the userID from the first row
        salt = myresult[0][0]
        debug("ID Found, Salt Validated: ")
        debug(salt)
        userFound = True;
        sqlString = "Select userID from user_table where HashedPass = %s and user_table.userName = %s"     
       
        password = salt + password
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password.encode())
        hash_hex = sha256_hash.hexdigest()
        debug(hash_hex)
        try:
            mycursor.execute(sqlString,(hash_hex,userName))
            myresult = mycursor.fetchall()
        except Exceptoin as e:
            print("Database Error: "+e)
        
        #Check if there is at least one result
        if myresult:
            # Extract the userID from the first row
            userID_id = myresult[0][0]
            debug("userID ID Found, Password Validated: "+str(userID_id))
            userAuth = True
            print("User Validated, preparing the adventure...")
            #update last log in
            proc_name = "UpdateLastLoginTime"
            mycursor.callproc(proc_name,(userID_id,))
            mydb.commit()
        else:
            # Handle the case where no matching records are found
            userID_id = None
            debug("Could Not Authenticate")



        
    else:
        # Handle the case where no matching records are found
        userID_id = None
        continue
#We are now in and Authenticated
     


mycursor.close()
mydb.close()
    
