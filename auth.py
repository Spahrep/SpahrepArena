import mysql.connector
import hashlib

#define a global variable for debugging
debug_on = False
def debug(string):
    if(debug_on):
        print (string)
    else:
        pass
    
def tryAgain():
    reply = input("Authentication Failed, try again (Y/N)?").lower()
    debug(reply)
    if  reply == "y":
        debug("A")
        return True
    else:
        debug("B")
        return False
    
def authUser(mydb):
    mycursor = mydb.cursor()
    isAuthenticated = False
    while not isAuthenticated:
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
            except Exception as e:
                print("Database Error: "+e)
        
            #Check if there is at least one result
            if myresult:
                # Extract the userID from the first row
                userID = myresult[0][0]
                debug("userID ID Found, Password Validated: "+str(userID))
                isAuthenticated = True
                print("User Validated, preparing the adventure...")
                #update last log in
                proc_name = "UpdateLastLoginTime"
                mycursor.callproc(proc_name,(userID,))
                mydb.commit()
            else:
                # Handle the case where no matching records are found
                userID = None
                debug("Could Not Authenticate")
                if tryAgain():
                    continue
                else:
                    return None   
        else:
            # Handle the case where no matching records are found
            userID = None
            debug("No Users Found")
            if tryAgain():
                continue
            else:
                return None
            
    return userID
