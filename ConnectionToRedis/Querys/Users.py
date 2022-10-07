import Database
import json
import Querys.Contacts as Contacts

def addUser(name, email):
    if not existUser(email):
        con = Database.openConnection()
        user = {}
        user['email']=email
        user['name']=name
        con.set(f"/users/{email}", json.dumps(user))
        con.close()
        print(chr(27)+"[1;32m"+f"User {name} added succesfully\n")
    else:
        print(chr(27)+"[1;31m"+f"User with email:{email} already exists\n")
    
def updateUser(email, username):
    if existUser(email):
        con = Database.openConnection()
        user = {}
        user['email']=email
        user['name']=username
        con.set(f"/users/{email}", json.dumps(user))
        con.close()
        print(chr(27)+"[1;32m"+f"User with email:{email} updated succesfully\n")
    else:
        print(chr(27)+"[1;31m"+f"User with email:{email} does not exist\n")

def listUsers():
    con = Database.openConnection()
    keys = con.keys('/users/*')
    if len(keys)!=0:
        print(chr(27)+"[1;33m"+"----------------USERS IN DB-----------------------")
        for key in keys: 
            user = con.get(key)
            user = json.loads(user)
            print(chr(27)+"[1;33m"+"--------------------------------------------------")
            print(chr(27)+"[1;37m"+"User name: "+user['name'])
            print(chr(27)+"[1;37m"+"Email: "+user['email'])
            
        con.close()
    else:
        print(chr(27)+"[1;31m"+f"There are no users in DB\n")
   
def existUser(email):
    con = Database.openConnection()
    keys = con.keys(f'/users/{email}')
    con.close()
    if len(keys)==0:
        return False
    else:
        return True

def getNameByEmail(email):
    con = Database.openConnection()
    keys = con.keys(f'/users/{email}')
    user = con.get(keys[0])
    user = json.loads(user)
    con.close()
    return user['name']
    
    

def removeUser(email):
    if existUser(email):
        con = Database.openConnection()
        con.delete(f'/users/{email}')
        print(chr(27)+"[1;32m"+f"User with email:{email} removed succesfully\n")
    else:
        print(chr(27)+"[1;31m"+f"User with email:{email} does not exist\n")