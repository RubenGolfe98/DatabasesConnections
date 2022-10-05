import sqlite3
import os

DB_NAME = "contacts.db"

def existsDB():
    existsDB=True
    con,cur = openConnectionAndCursor()
    try:
        cur.execute(f"SELECT * FROM users")
    except sqlite3.OperationalError:
        existsDB=False
    return existsDB

def openConnectionAndCursor():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    return con,cur

def closeConnectionAndCursor(con, cur):
    cur.close()
    con.close()

def create():
    con,cur = openConnectionAndCursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS contacts(email VARCHAR(32) PRIMARY KEY, 
                                            name VARCHAR(32) NOT NULL, 
                                            user VARCHAR(32),
                                            FOREIGN KEY(user) REFERENCES user(name))
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users(name VARCHAR(32) PRIMARY KEY,
                                         email VARCHAR(32))
    ''')
    print(chr(27)+"[1;32m"+"Database created\n")
    closeConnectionAndCursor(con,cur)

def destroyDB():
    os.remove(DB_NAME)
    print(chr(27)+"[1;32m"+"Database destroyed\n")

