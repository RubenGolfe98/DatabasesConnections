import sys
import json
import Database
import Console

def getKeysEqualsTo(email):
    con = Database.openConnection()
    keys = con.keys(f'/contacts/{email}')
    return keys

def numWordsEqualsTo(cad,num):
    if(len(cad) == num):
        return True
    else:
        Console.unknownCommand()
        return False

def addContact(username, email, tittle):
    if not existContact(username, email):
        con = Database.openConnection()
        contact = {}
        contact['email']=email
        contact['tittle']=tittle
        contact['username']=username
        con.set(f"/contacts/{email}", json.dumps(contact))
        con.close()
        print(chr(27)+"[1;32m"+f"Contact {tittle} added succesfully\n")
    else:
        print(chr(27)+"[1;31m"+f"Contact with email:{tittle} already exists\n")

def listContacts(username):
    con = Database.openConnection()
    keys = con.keys('/contacts/*')
    if len(keys)!=0:
        for key in keys: 
            contact = con.get(key)
            contact = json.loads(contact)
            if contact['username']==username:
                print(chr(27)+"[1;33m"+"--------------------------------------------------")
                print(chr(27)+"[1;37m"+"Contact name: "+contact['tittle'])
                print(chr(27)+"[1;37m"+"Email: "+contact['email'])
        con.close()
    else:
        print(chr(27)+"[1;31m"+f"You don't have contacts\n")

def existContact(username, email):
    con = Database.openConnection()
    keys = con.keys(f'/contacts/{email}')
    con.close()
    if len(keys)==0:
        return False
    else:
        for key in keys: 
            contact = con.get(key)
            contact = json.loads(contact)
            if contact['username']==username:
                return True
        return False

def updateContact(username, email, tittle):
    if existContact(username, email):
        con = Database.openConnection()
        contact = {}
        contact['email']=email
        contact['tittle']=tittle
        contact['username']=username
        con.set(f"/contacts/{email}", json.dumps(contact))
        con.close()
        print(chr(27)+"[1;32m"+f"Contact with email:{email} updated succesfully\n")
    else:
        print(chr(27)+"[1;31m"+f"Contact with email:{email} does not exist\n")

def removeContact(username, email):
    if existContact(username, email):
        con = Database.openConnection()
        con.delete(f'/contacts/{email}')
        print(chr(27)+"[1;32m"+f"Contact with email:{email} removed succesfully\n")
    else:
        print(chr(27)+"[1;31m"+f"Contact with email:{email} does not exist\n")