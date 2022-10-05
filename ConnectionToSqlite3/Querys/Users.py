import Database
import Querys.Contacts as Contacts

def addUser(name, email):
    if userInDB(name):
        print(chr(27)+"[1;31m"+f"User not added(User '{name}' is already in DB)\n")
    else:
        con,cur = Database.openConnectionAndCursor()
        cur.execute(f"INSERT INTO users VALUES('{name}','{email}')")
        con.commit()
        Database.closeConnectionAndCursor(con,cur)
        print(chr(27)+"[1;32m"+f"User {name} added succesful\n")
    
def updateUser(username, email):
    if userInDB(username):
        con,cur = Database.openConnectionAndCursor()
        cur.execute(f"UPDATE users SET email='{email}' WHERE name='{username}'")
        con.commit()
        Database.closeConnectionAndCursor(con,cur)
        print(chr(27)+"[1;32m"+f"{username} updated succesful\n")
    else:
        print(chr(27)+"[1;31m"+f"The user '{username}' does not exists in the database\n")

def listUsers():
    con,cur = Database.openConnectionAndCursor()
    cur.execute("SELECT * FROM users")
    res = cur.fetchall()
    if len(res)==0:
        print(chr(27)+"[1;31m"+"Database is empty\n")
    else:
        for row in res: 
            print(chr(27)+"[1;33m"+"--------------------------------------------------")
            print(chr(27)+"[1;37m"+"User name: ",row[0])
            print(chr(27)+"[1;37m"+"Email: ",row[1])
        print("")
    Database.closeConnectionAndCursor(con,cur)
   
def userInDB(name):
    con,cur = Database.openConnectionAndCursor()
    cur.execute(f"SELECT name FROM users WHERE name='{name}'")
    res = cur.fetchall()
    if len(res)==0:
        Database.closeConnectionAndCursor(con,cur)
        return False
    else:
        Database.closeConnectionAndCursor(con,cur)
        return True

def removeUser(name):
    if userInDB(name):
        con,cur = Database.openConnectionAndCursor()
        cur.execute(f"DELETE FROM users WHERE name='{name}'")
        con.commit()
        Database.closeConnectionAndCursor(con,cur)
        Contacts.removeContactByUser(name)
        print(chr(27)+"[1;32m"+f"User '{name}' removed succesful\n")
    else:
        print(chr(27)+"[1;31m"+f"User '{name}' does not exists in the database\n") 