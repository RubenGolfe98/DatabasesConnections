import Database

def addContact(userName, email, tittle):
    if contactInDB(email):
        print(chr(27)+"[1;31m"+f"Contact not added(Contact with email: '{email}' is already in DB)\n")
    else:
        con,cur = Database.openConnectionAndCursor()
        cur.execute(f"INSERT INTO contacts VALUES('{email}','{tittle}','{userName}')")
        con.commit()
        Database.closeConnectionAndCursor(con,cur)
        print(chr(27)+"[1;32m"+f"Contact {tittle} added succesful\n")
    

def listContacts(username):
    con,cur = Database.openConnectionAndCursor()
    cur.execute(f"SELECT * FROM contacts WHERE user ='{username}'")
    res = cur.fetchall()
    if len(res)==0:
        print(chr(27)+"[1;31m"+"You don't have contacts\n")
    else:
        print(chr(27)+"[1;33m"+f"---------------{username} Contacts---------------")
        for row in res: 
            print(chr(27)+"[1;37m"+"Email: ",row[0])
            print("Name:  ",row[1])
            print(chr(27)+"[1;33m"+"--------------------------------------------------")
        print("")
    Database.closeConnectionAndCursor(con,cur)
   

def updateContact(username, email, tittle):
    if contactInDB(email):
        if isYourContact(username, email):
            con,cur = Database.openConnectionAndCursor()
            cur.execute(f"UPDATE contacts SET name='{tittle}' WHERE email='{email}'")
            con.commit()
            Database.closeConnectionAndCursor(con,cur)
            print(chr(27)+"[1;32m"+f"Contact {tittle} updated succesful\n")
        else:
            print(chr(27)+"[1;31m"+f"You can not update '{tittle}' contact because is not yours \n")
    else:
        print(chr(27)+"[1;31m"+f"The contact '{tittle}' does not exists in the database\n")
    
    

def isYourContact(username, email):
    con,cur = Database.openConnectionAndCursor()
    cur.execute(f"SELECT name FROM contacts WHERE email='{email}' AND user='{username}'")
    res = cur.fetchall()
    if len(res)==0:
        Database.closeConnectionAndCursor(con,cur)
        return False
    else:
        Database.closeConnectionAndCursor(con,cur)
        return True

def removeContact(username, email):
    if contactInDB(email):
        if isYourContact(username, email):
            con,cur = Database.openConnectionAndCursor()
            cur.execute(f"DELETE FROM contacts WHERE email='{email}'")
            con.commit()
            Database.closeConnectionAndCursor(con,cur)
            print(chr(27)+"[1;32m"+f"Contact with email: '{email}' removed succesful\n")
        else:
            print(chr(27)+"[1;31m"+f"You can not remove '{email}' contact because is not yours \n")
    else:
        print(chr(27)+"[1;31m"+f"The contact with email: '{email}' does not exists in the database\n") 
    

def contactInDB(email):
    con,cur = Database.openConnectionAndCursor()
    cur.execute(f"SELECT name FROM contacts WHERE email='{email}'")
    res = cur.fetchall()
    if len(res)==0:
        Database.closeConnectionAndCursor(con,cur)
        return False
    else:
        Database.closeConnectionAndCursor(con,cur)
        return True

def removeContactByUser(username):
    con,cur = Database.openConnectionAndCursor()
    cur.execute(f"SELECT email FROM contacts WHERE user='{username}'")
    res = cur.fetchall()
    if len(res)!=0:
        for row in res: 
            removeContact(row[0])
        con.commit()
    Database.closeConnectionAndCursor(con,cur)
